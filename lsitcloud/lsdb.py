from django.shortcuts import render
from myadmin.models import Myadmin
from lsitcloud.models import lsitcloud
from django.http import JsonResponse
import boto3, json
# Initialize DynamoDB resource
session = boto3.Session(
    aws_access_key_id="AKIAZI2LE6EX5MT67CT5",
    aws_secret_access_key="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",
    region_name="ap-south-1"
)
dynamodb = session.client('dynamodb', region_name='ap-south-1')
resource = session.resource('dynamodb', region_name='ap-south-1')

def lsdbtables(request):
    default_theme = Myadmin.objects.get(key="default_theme")
    if request.session.get('email'):
        # Fetch the list of table names
        response = dynamodb.list_tables()
        table_names = response.get('TableNames', [])
        # Build table rows with details
        table_rows = ""
        for table_name in table_names:
            table_info = dynamodb.describe_table(TableName=table_name)
            table_details = table_info.get('Table', {})
            key_schema = table_details.get('KeySchema', [])
            primary_key = ", ".join([f"{key['AttributeName']} ({key['KeyType']})" for key in key_schema])

            # Append table row
            table_rows += f"""
                <tr>
                    <td><a href="lsdbtabledetails?tablename={table_details.get('TableName', 'N/A')}">{table_details.get('TableName', 'N/A')}</a></td>
                    <td>{primary_key}</td>
                    <td>{table_details.get('ItemCount', 'N/A')}</td>
                    <td>{table_details.get('TableSizeBytes', 'N/A')} bytes</td>
                    <td>{table_details.get('CreationDateTime', 'N/A')}</td>
                    <td>{table_details.get('TableStatus', 'N/A')}</td>
                </tr>
            """
        return render(request, "lsdbtables.html", {"default_theme": default_theme.value, "email": request.session.get('email'), "fullname": request.session.get('fullname'), "table_data": table_rows})
    else:
        return render(request, "login.html", {"default_theme": default_theme.value})

def lsdbapi(request):
    default_theme = Myadmin.objects.get(key="default_theme")
    if request.session.get('email'):
        return render(request, "lsdbapi.html", {"default_theme": default_theme.value, "email": request.session.get('email'), "fullname": request.session.get('fullname')})
    else:
        return render(request, "login.html", {"default_theme": default_theme.value})
    
def createtable(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            table_name = data.get('table_name', '').strip()
            primary_key = data.get('primary_key', '').strip()
            key_type = data.get('key_type', '').strip()
            cache = lsitcloud.objects.get(key=request.session.get('email'))
            # Create the table with on-demand capacity mode
            response = dynamodb.create_table(
                TableName=table_name,
                KeySchema=[
                    {'AttributeName': primary_key, 'KeyType': 'HASH'}
                ],
                AttributeDefinitions=[
                    {'AttributeName': primary_key, 'AttributeType': key_type}
                ],
                BillingMode='PAY_PER_REQUEST'  # Set on-demand billing mode
            )

            cache = json.loads(cache.value)
            cache["lsdb"]["lsdbtables"][response['TableDescription']['TableName']] = {
                "tablename": response['TableDescription']['TableName'],
                "primarykey": response['TableDescription']['KeySchema'][0]['AttributeName'],
                "createdon": response['TableDescription']['CreationDateTime'].strftime("%Y-%m-%d %H:%M:%S")
            }
            table = resource.Table('lsit-developments')
            table.put_item(Item=cache)
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

def lsdbtabledetails(request):
    default_theme = Myadmin.objects.get(key="default_theme")
    if request.session.get('email'):
        query = request.GET.get('tablename', '')
        if not query:
            return "Table name is required", 400
        table = resource.Table(query)
        # Describe the table to get the key schema
        try:
            table_info = dynamodb.describe_table(TableName=query)
        except dynamodb.exceptions.ResourceNotFoundException:
            return "Table not found", 404
        
        table_details = table_info.get('Table', {})
        key_schema = table_details.get('KeySchema', [])
        # Get primary key(s) in the format "AttributeName (KeyType)"
        primary_keys = [key['AttributeName'] for key in key_schema]

        # Perform the scan operation
        response = table.scan()
        items = response['Items']

        if not items:
            return render(request, "lsdbtabledetails.html", {"default_theme": default_theme.value, "email": request.session.get('email'), "fullname": request.session.get('fullname'), "tableitems": '<table class="table table-bordered text-nowrap border-bottom" id="responsive-datatable"><thead><tr><th></th></tr></thead><tbody></tbody></table>'})

        # Generate the headers, prioritizing primary keys first
        headers = ''.join(f"<th class='wd-20p'>{key} (Primary Key)</th>" for key in primary_keys)
        other_headers = ''.join(
            f"<th class='wd-20p'>{header}</th>" for header in items[0].keys() if header not in primary_keys
        )
        headers += other_headers

        # Generate the rows, ensuring primary keys appear first
        rows = ''.join(
            f"<tr>"
            + ''.join(f"<td><a href='lsdbtableitems?tablename={query}&primarykey={key}&primarykeyvalue={item.get(key, '')}'>{item.get(key, '')}<a></td>" for key in primary_keys)
            + ''.join(f"<td>{json_to_ul(item.get(header, ''))}</td>" for header in items[0].keys() if header not in primary_keys)
            + f"</tr>"
            for item in items
        )

        # Generate the final HTML table
        final_html = f"""
            <table class="table table-bordered text-nowrap border-bottom" id="responsive-datatable">
                <thead>
                    <tr>
                        {headers}
                    </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>
        """
        return render(request, "lsdbtabledetails.html", {"default_theme": default_theme.value, "email": request.session.get('email'), "fullname": request.session.get('fullname'), "tableitems": final_html})
    else:
        return render(request, "login.html", {"default_theme": default_theme.value})

def lsdbtableitems(request):
    default_theme = Myadmin.objects.get(key="default_theme")
    if request.session.get('email'):
        tablename = request.GET.get('tablename', '')
        primarykey = request.GET.get('primarykey', '')
        primarykeyvalue = request.GET.get('primarykeyvalue', '')
        # Access the DynamoDB table
        table = resource.Table(tablename)
        # Get the item from DynamoDB using the primary key
        response = table.get_item(Key={primarykey: primarykeyvalue})
        item = response.get('Item')
        return render(request, "lsdbtableitems.html", {"default_theme": default_theme.value, "email": request.session.get('email'), "fullname": request.session.get('fullname'), "tablename": tablename,"schema": json.dumps(item)})
    else:
        return render(request, "login.html", {"default_theme": default_theme.value})
    
def lsdbputitems(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            tablename = data.get('tablename', '')
            tabledata = data.get('tabledata', '')
            table = resource.Table(tablename)
            table.put_item(Item=tabledata)
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

def json_to_ul(data):
    if isinstance(data, dict):
        ul = '<ul>'
        for key, value in data.items():
            ul += f'<li>'
            ul += f'<span class="fs-8">{key}</span> : '
            if isinstance(value, dict) or isinstance(value, list):
                ul += json_to_ul(value)
            else:
                ul += f'<span class="fs-8">{value}</span>'
            ul += '</li>'
        ul += '</ul>'
        return ul
    elif isinstance(data, list):
        ul = '<ul>'
        for item in data:
            ul += f'<li>'
            if isinstance(item, dict) or isinstance(item, list):
                ul += json_to_ul(item)
            else:
                ul += f'{item}'
            ul += '</li>'
        ul += '</ul>'
        return ul
    else:
        return str(data)