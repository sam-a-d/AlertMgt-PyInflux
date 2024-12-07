from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = "EDFGsul_l3hXK9y6BMVgspGSpnvVmabw_Ly2veGjshM9B31ykmRife_KQTt2ffsqAfde8tZGMcbmxQ4_oIEEeQ=="
org = "softArc"
bucket = "testBuck"
url="http://localhost:8086"

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
    
    # for table in tables:
    #     for record in table.records:
    #         # print(dir(record))
    #         # break
    #         print("Time: ", record.get_time(), "field", record.get_field(), "value: ", record.get_value())
