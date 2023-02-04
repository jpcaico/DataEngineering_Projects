import pandas as pd
from kafka import  KafkaProducer
from time import sleep
from json import dumps
import json
import time


producer = KafkaProducer(bootstrap_servers=['52.3.254.234:9092'],
                        value_serializer=lambda x:dumps(x).encode('utf-8')
)

df = pd.read_csv("data/stock_data.csv")

while True:
    dict_stock = df.sample(1).to_dict(orient='records')[0]
    producer.send('demo_test', value=dict_stock)
    producer.flush()
    time.sleep(1)

