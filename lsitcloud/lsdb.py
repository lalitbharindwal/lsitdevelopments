from django.shortcuts import render
from myadmin.models import Myadmin
from lsitcloud.models import lsitcloud
from django.http import JsonResponse
import simplejson as json
from decimal import Decimal
import boto3
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
        cache = json.loads(lsitcloud.objects.get(key=request.session.get('email')).value)
        # Build table rows with details
        table_rows = ""
        for table_name in cache['lsdb']['lsdbtables'].keys():
            table_info = dynamodb.describe_table(TableName=table_name)
            table_details = table_info.get('Table', {})

            # Append table row
            table_rows += f"""
                <tr>
                    <td><a href="lsdbtabledetails?tablename={table_details.get('TableName', 'N/A')}">{table_details.get('TableName', 'N/A')}</a></td>
                    <td>{cache['lsdb']['lsdbtables'][table_name]['primarykey']}</td>
                    <td>{table_details.get('ItemCount', 'N/A')}</td>
                    <td>{table_details.get('TableSizeBytes', 'N/A')} bytes</td>
                    <td>{cache['lsdb']['lsdbtables'][table_name]['createdon']}</td>
                    <td>{table_details.get('TableStatus', 'N/A')}</td>
                    <td><a href="lsdbtabledetails?tablename={table_details.get('TableName', 'N/A')}"><button class="btn btn-primary"><i class="fas fa-eye"></i></button></a> <button class="btn btn-danger" onclick="deletetable('{table_details.get('TableName', 'N/A')}')"><i class="far fa-trash-alt"></i></button></td>
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
    
def lsdbcreatetable(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            tablename = data.get('tablename', '').strip()
            primarykey = data.get('primarykey', '').strip()
            keytype = data.get('keytype', '').strip()
            cache = lsitcloud.objects.get(key=request.session.get('email'))
            # Create the table with on-demand capacity mode
            response = dynamodb.create_table(
                TableName=tablename,
                KeySchema=[
                    {'AttributeName': primarykey, 'KeyType': 'HASH'}
                ],
                AttributeDefinitions=[
                    {'AttributeName': primarykey, 'AttributeType': keytype}
                ],
                BillingMode='PAY_PER_REQUEST'  # Set on-demand billing mode
            )

            items = json.loads(cache.value)
            items["lsdb"]["lsdbtables"][response['TableDescription']['TableName']] = {
                "tablename": response['TableDescription']['TableName'],
                "primarykey": response['TableDescription']['KeySchema'][0]['AttributeName'],
                "primarykeytype": response['TableDescription']['AttributeDefinitions'][0]['AttributeType'],
                "createdon": response['TableDescription']['CreationDateTime'].strftime("%Y-%m-%d %H:%M:%S")
            }
            table = resource.Table('lsit-developments')
            table.put_item(Item=items)
            cache.value = json.dumps(items)
            cache.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

def lsdbtabledetails(request):
    default_theme = Myadmin.objects.get(key="default_theme")
    if request.session.get('email'):
        tablename = request.GET.get('tablename', '')
        if not tablename:
            return "Table name is required", 400
        table = resource.Table(tablename)
        # Describe the table to get the key schema
        try:
            table_info = dynamodb.describe_table(TableName=tablename)
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
            return render(request, "lsdbtabledetails.html", {"default_theme": default_theme.value, "email": request.session.get('email'), "fullname": request.session.get('fullname'), "tablename": tablename, "tableitems": '<table class="table table-bordered text-nowrap border-bottom" id="responsive-datatable"><thead><tr><th></th></tr></thead><tbody></tbody></table>'})

        # Generate the final HTML table
        final_html = json_to_table(items, primary_keys, tablename)
        return render(request, "lsdbtabledetails.html", {"default_theme": default_theme.value, "email": request.session.get('email'), "fullname": request.session.get('fullname'), "tablename": tablename, "tableitems": final_html})
    else:
        return render(request, "login.html", {"default_theme": default_theme.value})

def json_to_table(json_data, primary_keys, tablename):
    def collect_keys(data):
        keys = set()
        for item in data:
            if isinstance(item, dict):
                for key, value in item.items():
                    keys.add(key)
                    if isinstance(value, dict) or isinstance(value, list):
                        keys.update(collect_keys([value]))
            elif isinstance(item, list):
                keys.update(collect_keys(item))
        return keys

    # Gather all keys from the data
    all_keys = collect_keys(json_data)
    other_keys = [key for key in all_keys if key not in primary_keys]

    # Start the table
    table_html = "<table class='table'>"

    # Generate headers
    headers = ""
    for key in primary_keys:
        headers += f"<th class='wd-15p'>{key} (Primary Key)</th>"
    for key in other_keys:
        headers += f"<th class='wd-10p'>{key}</th>"
    headers += "<th class='wd-20p'>Actions</th>"  # Add Actions header
    table_html += f"<thead><tr>{headers}</tr></thead>"

    # Generate rows
    rows = ""
    for item in json_data:
        row = "<tr>"
        # Add primary key values with links
        for key in primary_keys:
            value = resolve_nested_value(item, key)
            row += f"<td><a href='lsdbtableitems?tablename={tablename}&primarykeyvalue={value}'>{value}</a></td>"
        # Add other keys
        for key in other_keys:
            value = resolve_nested_value(item, key)
            row += f"<td>{json_to_ul(value)}</td>"
            # Add delete button
    
        for key in primary_keys:
            value = resolve_nested_value(item, key)
            row += f"<td><button class='btn btn-danger' onclick='deleteattribute(\"{tablename}\", \"{value}\")'><i class=\"far fa-trash-alt\"></i></button></td>"
        row += "</tr>"
        rows += row

    # Add rows to the table
    table_html += f"<tbody>{rows}</tbody>"

    # End the table
    table_html += "</table>"

    return table_html


# Helper function to resolve nested keys dynamically
def resolve_nested_value(data, key):
    if isinstance(data, dict) and key in data:
        return data[key]
    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, (dict, list)):
                result = resolve_nested_value(v, key)
                if result is not None:
                    return result
    if isinstance(data, list):
        for item in data:
            result = resolve_nested_value(item, key)
            if result is not None:
                return result
    return ""


# Helper function to convert nested JSON into <ul>
def json_to_ul(value):
    if isinstance(value, dict):
        return "<ul>" + "".join(f"<li>{k}: {json_to_ul(v)}</li>" for k, v in value.items()) + "</ul>"
    elif isinstance(value, list):
        return "<ul>" + "".join(f"<li>{json_to_ul(v)}</li>" for v in value) + "</ul>"
    else:
        return str(value)


def lsdbtableitems(request):
    default_theme = Myadmin.objects.get(key="default_theme")
    if request.session.get('email'):
        tablename = request.GET.get('tablename', '')
        cache = json.loads(lsitcloud.objects.get(key=request.session.get('email')).value)
        primarykey = cache['lsdb']['lsdbtables'][tablename]['primarykey']
        primarykeyvalue = request.GET.get('primarykeyvalue', '')
        if(primarykeyvalue):
            # Access the DynamoDB table
            table = resource.Table(tablename)
            # Get the item from DynamoDB using the primary key
            response = table.get_item(Key={primarykey: primarykeyvalue})
            item = response.get('Item')
            return render(request, "lsdbtableitems.html", {"default_theme": default_theme.value, "email": request.session.get('email'), "fullname": request.session.get('fullname'), "tablename": tablename,"schema": json.dumps(item)})
        else:
            blankitem = {}
            blankitem[primarykey] = ""
            return render(request, "lsdbtableitems.html", {"default_theme": default_theme.value, "email": request.session.get('email'), "fullname": request.session.get('fullname'), "tablename": tablename,"schema": json.dumps(blankitem)})
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
        
def lsdbdeletetable(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            tablename = data.get('tablename', '').strip()
            cache = lsitcloud.objects.get(key=request.session.get('email'))
            dynamodb.delete_table(TableName=tablename)
            items = json.loads(cache.value)
            del items["lsdb"]["lsdbtables"][tablename]
            cache.value = json.dumps(items)
            cache.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

def lsdbdeleteattribute(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            tablename = data.get('tablename', '').strip()
            primarykeyvalue = data.get('primarykeyvalue', '').strip()
            cache = json.loads(lsitcloud.objects.get(key=request.session.get('email')).value)
            # Construct the Key
            key = {cache['lsdb']['lsdbtables'][tablename]['primarykey']: {cache['lsdb']['lsdbtables'][tablename]['primarykeytype']: primarykeyvalue}}
            # Perform the delete operation
            dynamodb.delete_item(
                TableName=tablename,
                Key=key
            )
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