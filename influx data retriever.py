from datetime import datetime

import os
from dotenv import load_dotenv
load_dotenv()

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = os.getenv('INFLUX_ACCESS_TOKEN')
org = os.getenv('INFLUX_ORG')
bucket = os.getenv('INFLUX_BUCKET')
url = os.getenv('INFLUX_URL')

import pandas as pd
with InfluxDBClient(url=url, token=token, org=org) as client:

    query = 'from(bucket: "testBuck") |> range(start: -5h)'
    tables = client.query_api().query(query, org=org)
    
    data = []

    for table in tables:
        for record in table.records:
            data.append({
                "time": record.get_time(),
                "field": record.get_field(),
                "value": record.get_value()
            })

    df = pd.DataFrame(data)
    print(df)
    