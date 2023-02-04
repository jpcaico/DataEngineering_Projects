import pandas as pd
from kafka import KafkaConsumer
from time import sleep
from json import dumps, loads
import json
from s3fs import S3FileSystem

s3 = S3FileSystem()


consumer = KafkaConsumer('demo_test',
                        bootstrap_servers=['52.3.254.234:9092'],
                        value_deserializer=lambda x:loads(x.decode('utf-8'))
)

for count, i in enumerate(consumer):
    with s3.open(f"s3://stock-analysis-jpcaico/stock_market_{count}.json", 'w') as file:
        json.dump(i.value, file)
