import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
call_redirect_url = os.environ.get("CALL_REDIRECT_URL")
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)


call = client.calls.create(
    url=f"{call_redirect_url}/voice",
    to=os.environ.get('TO_PHONE_NUMBER'),
    from_=os.environ.get('TWILIO_PHONE_NUMBER'),
)
