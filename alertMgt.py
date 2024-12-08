from telegramSender import TelegramSender # Local Module - github user: sam-a-d
from dataAnalyzer import DataAnalyzer

import os, time
from dotenv import load_dotenv
load_dotenv(override=True)

# You can generate an API token from the "API Tokens Tab" in the UI
token = os.getenv('INFLUX_ACCESS_TOKEN')
org = os.getenv('INFLUX_ORG')
bucket = os.getenv('INFLUX_BUCKET')
url = os.getenv('INFLUX_URL')
telegram_bot_tocken = os.getenv('TELEGRAM_BOT_API')

chat_id = [7325990260]

def send_alert(message="Risky Condition", chat_id=[7325990260]):

    message = message
    chat_id = chat_id

    T = TelegramSender(telegram_bot_tocken, chat_id=chat_id)
    response = T.send_message(message=message)
    print(response)

D = DataAnalyzer(token=token, org=org, bucket=bucket, url=url, water_thres=4.7, rain_thres=950)

while True:
    # chek if the condition is risky
    if D.get_riskCondition():
        send_alert(message='Risky')
    break
