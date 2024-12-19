import smtplib, whois, json, requests, boto3
import dns.resolver
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.http import JsonResponse
from django.shortcuts import render
from techmark.models import techmark
session = boto3.Session(
    aws_access_key_id="AKIAZI2LE6EX5MT67CT5",
    aws_secret_access_key="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",
    region_name="ap-south-1"
)
dynamodb = session.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('techmark-solutions')
# SMTP configurations for known providers
providers = {
    'gmail.com': {'smtp_server': 'smtp.gmail.com', 'smtp_port': 587, 'use_tls': True},
    'yahoo.com': {'smtp_server': 'smtp.mail.yahoo.com', 'smtp_port': 587, 'use_tls': True},
    'outlook.com': {'smtp_server': 'smtp-mail.outlook.com', 'smtp_port': 587, 'use_tls': True},
    'hotmail.com': {'smtp_server': 'smtp-mail.outlook.com', 'smtp_port': 587, 'use_tls': True},
    'secureserver.net': {'smtp_server': 'smtpout.secureserver.net', 'smtp_port': 587, 'use_tls': False},
    # Add more providers as needed
}

def get_whois_info(domain):
    try:
        domain_info = whois.whois(domain)
        return domain_info
    except Exception as e:
        return None
    
def get_dns_records(domain):
    try:
        records = {}
        # A (IP Address) records
        a_records = dns.resolver.resolve(domain, 'A')
        records['A'] = [ip.to_text() for ip in a_records]
        
        # MX (Mail Exchanger) records
        mx_records = dns.resolver.resolve(domain, 'MX')
        records['MX'] = [mx.exchange.to_text() for mx in mx_records]
        
        # NS (Name Server) records
        ns_records = dns.resolver.resolve(domain, 'NS')
        records['NS'] = [ns.to_text() for ns in ns_records]
        
        # TXT records
        try:
            txt_records = dns.resolver.resolve(domain, 'TXT')
            records['TXT'] = [txt.to_text() for txt in txt_records]
        except dns.resolver.NoAnswer:
            records['TXT'] = []
        
        return records
    except Exception as e:
        return None
    
def get_smtp_server(dns_info):
    mx_record = dns_info["MX"][0]
    if mx_record:
        # Infer the SMTP server from the MX record
        if 'google' in mx_record:
            return 'smtp.gmail.com'
        elif 'outlook' in mx_record or 'hotmail' in mx_record:
            return 'smtp-mail.outlook.com'
        elif 'secureserver' in mx_record or 'godaddy' in mx_record:
            return 'smtpout.secureserver.net'
        elif 'hostinger' in mx_record:
            return 'smtp.hostinger.com'
        elif 'yahoo' in mx_record:
            return 'smtp.mail.yahoo.com'
        elif 'zoho' in mx_record:
            return 'smtp.zoho.com'
        elif 'amazonaws' in mx_record:
            return 'email-smtp.us-east-1.amazonaws.com'
        else:
            return False
    else:
        return None
    
def get_ip_info(ip):
    try:
        # Using ipinfo.io API for IP geolocation and other info
        response = requests.get(f"http://ipinfo.io/{ip}/json")
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        return None

def domain_info(domain):
    whois_info = get_whois_info(domain)
    dns_info = get_dns_records(domain)
    # If you want to gather info about the A (IP Address) records:
    if(dns_info is not None):
        smtp_server = get_smtp_server(dns_info)
        if 'A' in dns_info:
            for ip in dns_info['A']:
                ip_info = get_ip_info(ip)
                payload = {
                    "domaininfo": {
                        "whoisinfo": whois_info,
                        "dnsinfo": dns_info,
                        "ipinfo": ip_info,
                        "smtp_server": smtp_server
                    }
                }
                return payload
    else:
        payload = {
                    "domaininfo": {
                        "whoisinfo": whois_info,
                        "dnsinfo": None,
                        "ipinfo": None,
                        "smtp_server": None
                    }
                }
        return payload

def check_smtp_login(smtp_server, smtp_port, email, password):
    try:
        # Create an SMTP session
        server = smtplib.SMTP(smtp_server, smtp_port)
        # Start TLS for security
        server.starttls()
        # Try to log in to the server with the provided credentials
        server.login(email, password)
        # If login succeeds, close the connection and return True
        server.quit()
        return True

    except smtplib.SMTPAuthenticationError:
        # Authentication failed
        return False
    except smtplib.SMTPException as e:
        # General SMTP-related error
        return False
    except Exception as e:
        # Any other error
        return False

# Custom function to convert datetime objects to ISO format
def json_default(value):
    if isinstance(value, datetime):
        return value.isoformat()

def send_email(event):
    try:
        # Extract data from the event dictionary
        sender_name = event.get("name")
        sender_email = event.get("email")
        user_email = event.get("useremail")
        user_password = event.get("password")
        recipient_email = event.get("to")
        cc_emails = event.get("cc", "")
        bcc_emails = event.get("bcc", "")
        reply_to = event.get("replyto", "")
        subject = event.get("subject")
        body_text = event.get("body_text")
        body_html = event.get("body_html")
        smtp_server = event.get("smtp_server")
        smtp_port = 587

        # Create a MIME message object
        msg = MIMEMultipart("alternative")
        msg['From'] = f"{sender_name} <{sender_email}>"
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Add CC and Reply-To if present (BCC is not added to headers)
        if cc_emails:
            msg['Cc'] = cc_emails
        if reply_to:
            msg.add_header('Reply-To', reply_to)

        # Attach plain text and HTML parts
        if body_text:
            msg.attach(MIMEText(body_text, 'plain'))
        if body_html:
            msg.attach(MIMEText(body_html, 'html'))

        # Create the complete recipient list (To + CC + BCC)
        recipients = [recipient_email] + cc_emails.split(",") + bcc_emails.split(",")

        # Create an SMTP session
        server = smtplib.SMTP(smtp_server, smtp_port)

        # Start TLS for security
        server.starttls()

        # Log in to the SMTP server using credentials
        server.login(user_email, user_password)

        # Send the email
        server.sendmail(user_email, recipients, msg.as_string())

        # Close the server connection
        #server.quit()

        # Return success message
        return {
            "status": "success",
            "message": None
        }

    except smtplib.SMTPAuthenticationError:
        # Handle incorrect email/password
        return {
            "status": "error",
            "message": "Authentication failed: Invalid username or password."
        }

    except smtplib.SMTPRecipientsRefused as e:
        # Handle rejected recipients
        return {
            "status": "error",
            "message": f"One or more recipients were refused.{str(e.recipients)}"
        }

    except smtplib.SMTPConnectError as e:
        # Handle connection issues
        return {
            "status": "error",
            "message": f"Failed to connect to the SMTP server: {str(e)}"
        }

    except smtplib.SMTPDataError as e:
        # Handle issues with the email data (e.g., size limits)
        return {
            "status": "error",
            "message": f"SMTP data error: {str(e)}"
        }

    except smtplib.SMTPException as e:
        # Handle other SMTP-related errors
        return {
            "status": "error",
            "message": f"An SMTP error occurred: {str(e)}"
        }

    except Exception as e:
        # Handle all other exceptions
        return {
            "status": "error",
            "message": f"An error occurred: {str(e)}"
        }

def addcampaign(request):
    if request.session.get('email'):
        cache = json.loads(techmark.objects.get(key=request.session.get('email')).value)
        active_aliases = ""
        senders = ""
        for key in cache["email-campaigns"]["email-credentials"].keys():
            active_aliases += f"""<tr>
                 <td data-label="Name">{cache["email-campaigns"]["email-credentials"][key]["sendername"]}</td>
                 <td data-label="Sender">{cache["email-campaigns"]["email-credentials"][key]["newaliasemail"]}</td>
                 <td data-label="Useremail">{cache["email-campaigns"]["email-credentials"][key]["senderemail"]}</td>
                 <td data-label="Verified on">{cache["email-campaigns"]["email-credentials"][key]["createdon"]}</td>
                 <td data-label="Status">Select</td>
                </tr>"""
            senders += f"<a class='dropdown-item' href='javascript:void(0);'>{cache["email-campaigns"]["email-credentials"][key]["newaliasemail"]}</a>"
        return render(request, "addcampaign.html", {"active_aliases": active_aliases, "senders": senders})
    else:
        return render(request, "techmarklogin.html")

def createalias(request):
    if request.method == 'POST':
        # Get input from form
        credential = json.loads(request.body)
        senderemail = credential["senderemail"]
        aliasemail = credential["newaliasemail"]
        password = credential["newemailpassword"]
        smtp_port = 587
        domaininfo = domain_info(senderemail.split('@')[-1])
        if(domaininfo["domaininfo"]["dnsinfo"]):
            if(check_smtp_login(domaininfo["domaininfo"]["smtp_server"], smtp_port, senderemail, password)):
                cache = techmark.objects.get(key=request.session.get('email'))
                key = {'email': request.session.get('email')}
                update_expression = "SET #emailcampaigns.#emailcredentials.#newemail = :data"
                expression_attribute_names = {
                    '#emailcampaigns': 'email-campaigns',
                    '#emailcredentials': 'email-credentials',
                    '#newemail': aliasemail
                }
                expression_attribute_values = {
                    ':data': credential
                }
                table.update_item(
                    Key=key,
                    UpdateExpression=update_expression,
                    ExpressionAttributeValues=expression_attribute_values,
                    ExpressionAttributeNames=expression_attribute_names
                )
                items = json.loads(cache.value)
                items["email-campaigns"]["email-credentials"][aliasemail] = credential
                cache.value = json.dumps(items)
                cache.save()
                # Define the key of the item to be updated
                return JsonResponse({
                    "success": True,
                    "domaininfo": json.dumps(domaininfo, default=json_default),
                    "message": "Verification Successful",
                    "items": items["email-campaigns"]["email-credentials"]
                })

            else:
                return JsonResponse({
                    "success": False,
                    "domaininfo": json.dumps(domaininfo, default=json_default),
                    "message": "Verification Failed"
                })
        else:
            return JsonResponse({
                    "success": None,
                    "domaininfo": json.dumps(domaininfo, default=json_default),
                    "message": "Verification Unsuccessful"
                })