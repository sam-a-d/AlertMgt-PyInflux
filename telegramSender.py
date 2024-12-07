import os
from dotenv import load_dotenv
load_dotenv()

import requests

class TelegramSender:

    def __init__(self, bot_token, chat_id, message='Risky Condition'):
        self.bot_tocken = bot_token
        self.chat_id = chat_id
        self.message = message

        self.url = f"https://api.telegram.org/bot{self.bot_tocken}/sendMessage"

    def send_message(self, **kwargs):

        self.message = kwargs['message'] if 'message' in kwargs else self.message
        self.chat_id = kwargs['chat_id'] if 'chat_id' in kwargs else self.chat_id

        payload = {
            "chat_id": self.chat_id,  # The target user's chat ID
            "text": self.message,     # The message to send
        }

        response = requests.post(self.url, data=payload)

        if response.status_code == 200:
            return 'Sending success'
        else:
            return 'Sending failed'
