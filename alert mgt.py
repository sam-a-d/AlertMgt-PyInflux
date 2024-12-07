# from random import Random
from datetime import datetime
import sensor

import os
from dotenv import load_dotenv
load_dotenv()

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = os.getenv('INFLUX_ACCESS_TOKEN')
org = os.getenv('INFLUX_ORG')
bucket = os.getenv('INFLUX_BUCKET')
url = os.getenv('INFLUX_URL')
telegram_bot_tocken = os.getenv('TELEGRAM_BOT_API')


import requests

def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,  # The target user's chat ID
        "text": message,     # The message to send
    }
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print("Failed to send message.")
        print(response.text)

chat_id = 7325990260
message = "This is a test message sent from the bot."
send_telegram_message(telegram_bot_tocken, chat_id, message)