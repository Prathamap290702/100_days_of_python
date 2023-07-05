from twilio.rest import Client
import os
import smtplib

TWILIO_SID = os.environ.get("T_SID")
TWILIO_AUTH_TOKEN = os.environ.get("T_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.environ.get("T_VIRTUAL_NUMBER")
TWILIO_VERIFIED_NUMBER = os.environ.get("YOUR_NUMBER")
MY_EMAIL = os.environ.get("YOUR_EMAIL")
MY_PASSWORD = os.environ.get("YOUR_PASSWORD")
MAIL_PROVIDER_SMTP_ADDRESS = "Mail providers SMTP address here"
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )