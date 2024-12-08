
from dotenv import load_dotenv
load_dotenv()

from influxdb_client import InfluxDBClient

class DataAnalyzer:

    def __init__(self, token, org, bucket, url, water_thres=4.5, rain_thres=950):
        
        self.token = token
        self.org = org
        self.bucket = bucket
        self.url = url
        self.water_thres = water_thres
        self.rain_thres = rain_thres

    def __queryGenerator(self, **kwargs):
        # water=900, rain=4.5
        # {'water': 900,
        #  'rain': 4.5,
        # }
        query = str()

        for k, v in kwargs.items():
            q = f'(r["_field"] == "{k}" and r["_value"] >= {v}) or'
            query += q
        return query
        


    def __retriveAndStoreData(self):

        with InfluxDBClient(url=self.url, token=self.token, org=self.org) as client:
            query = f'''
                from(bucket: "{self.bucket}")
                |> range(start: -5h)
                |> filter(fn: (r) => r["_measurement"] == "SensorValues")
                |> filter(fn: (r) => 
                    {self.__queryGenerator(water=self.water_thres, rain=self.rain_thres)}
                    r["_field"] == "area"
                    or r["_field"] == "region"
                )
                |> group(columns: ["_time","_field"])
                |> yield(name: "mean")
            '''

            tables = client.query_api().query(query, org=self.org)

        # Initialize a dictionary to group records by time
        grouped_data = {}

        for table in tables:
            for record in table.records:
                time = record.get_time()
                field = record.get_field()
                value = record.get_value()
                
                # Access tags through the 'tags' attribute, which is usually a dictionary
                tags = record.values.get("tags", {})

                # Group records by their timestamp
                if time not in grouped_data:
                    grouped_data[time] = {
                                            "region": record.values.get('region'),
                                            "area"  : record.values.get('area')
                                        }  # Store the tags at the timestamp level
                
                # Add the field and its value to the timestamp group
                grouped_data[time][field] = value

        # Filter data based on the condition and create the final list
        data = []

        for time, fields in grouped_data.items():
            # Check if both 'water' and 'rain' fields satisfy the condition
            if fields.get("water", 0) > self.water_thres and fields.get("rain", 0) > self.rain_thres:
                data.append({
                    "time": time,
                    "water": fields.get("water"),
                    "rain": fields.get("rain"),
                    "area": fields.get("area"),
                    "region": fields.get("region"),
                })

        return data

    def get_filteredData(self):
        return self.__retriveAndStoreData()

    def get_riskCondition(self):
        return True if len(self.get_filteredData()) >= 1 else False
