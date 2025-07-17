
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)
def send_rem(date,rem):
    message = client.messages.create(
                                  from_='whatsapp:+14155238886',
                                  body='*REMINDER* '+date+'\n'+rem,
                                  to='whatsapp:+26778072443'
                              )
     
    print(message.sid)
