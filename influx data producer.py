# from random import Random
from datetime import datetime
import sensor
import time, os

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


with InfluxDBClient(url=url, token=token, org=org) as client:
    
    S = sensor.Sensor()
    write_api = client.write_api(write_options=SYNCHRONOUS)

    for i in range(3):
    
        point = Point("SensorValues")\
        .tag('risk', S.get_tag())\
        .field("Temp", S.getTemp())\
        .field("Hum", S.getHumidity())\
        .field("SoilMoist", S.getSoilMoist())\

        time.sleep(3)
        write_api.write(bucket, org, point)

client.close()