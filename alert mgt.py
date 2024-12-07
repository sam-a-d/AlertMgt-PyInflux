# from random import Random
from datetime import datetime
import sensor

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

