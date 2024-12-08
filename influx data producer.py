# from random import Random
from datetime import datetime
import sensor # Local Module - github user: sam-a-d
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

    for i in range(1000):
    
        point = Point("SensorValues")\
        .tag("area", S.getArea())\
        .tag("region", S.getRegion())\
        .field("rain",S.getCumulativeRainfall())\
        .field("flow",S.getFlowVelocity())\
        .field("soilSat",S.getSoilSaturation())\
        .field("water",S.getWaterLevel())\
        .field("wind",S.getWindSpeed())\
        
        time.sleep(1)
        write_api.write(bucket, org, point)

client.close()