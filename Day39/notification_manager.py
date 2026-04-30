import os
from twilio.rest import Client


class NotificationManager:
    """
    This class is responsible for sending notifications with the deal flight details.
    """
    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])

    def send_sms(self, message_body):
        """
        Send a sms message
        :param message_body:
        :return:
        """
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["TWILIO_VERIFIED_NUMBER"]
        )
        # Prints if successfully sent.
        print(message.sid)


    def send_whatsapp(self, message_body):
        """
        Send a whatsapp message
        :param message_body:
        :return:
        """
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.sid)
