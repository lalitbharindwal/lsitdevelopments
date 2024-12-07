from django.shortcuts import render
from myadmin.models import Myadmin
from django.http import JsonResponse
import boto3, json
# Initialize DynamoDB resource
session = boto3.Session(
    aws_access_key_id="AKIAZI2LE6EX5MT67CT5",
    aws_secret_access_key="ixYVq+GE4A6xxeWlcGxajyZ92mRe5M0LxNoq0fyq",
    region_name="ap-south-1"
)
#dynamodb = session.resource('dynamodb', region_name='ap-south-1')  # Use your AWS region
dynamodb = session.client('dynamodb', region_name='ap-south-1')

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
            
            # Extract key schema
            key_schema = table_details.get('KeySchema', [])
            primary_key = ", ".join([f"{key['AttributeName']} ({key['KeyType']})" for key in key_schema])

            # Append table row
            table_rows += f"""
                <tr>
                    <td>{table_details.get('TableName', 'N/A')}</td>
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

            # Validation logic here

            # Create the table with on-demand capacity mode
            dynamodb.create_table(
                TableName=table_name,
                KeySchema=[
                    {'AttributeName': primary_key, 'KeyType': 'HASH'}
                ],
                AttributeDefinitions=[
                    {'AttributeName': primary_key, 'AttributeType': key_type}
                ],
                BillingMode='PAY_PER_REQUEST'  # Set on-demand billing mode
            )
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})