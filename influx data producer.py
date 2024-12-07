# from random import Random
from datetime import datetime
import sensor
import time


from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = "ybnvxMPciOeiyM9FgzNIKTxvcIZK8YCgfO_EC9pUHoPyclWjxhQCG_ghD3T7kwLjGWxX3kAUGkoXRAVeKEndNg=="
org = "softArc"
bucket = "pythonBucket"
url = "http://localhost:8086"


with InfluxDBClient(url=url, token=token, org=org) as client:
    
    S = sensor.Sensor()
    write_api = client.write_api(write_options=SYNCHRONOUS)

    for i in range(50):
        point = Point("SensorValues")\
        .tag('risk', S.get_tag())\
        .field("Temp", S.getTemp())\
        .field("Hum", S.getHumidity())\
        .field("SoilMoist", S.getSoilMoist())\

        time.sleep(.2)
        write_api.write(bucket, org, point)

client.close()