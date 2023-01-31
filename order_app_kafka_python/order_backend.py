import json
import time

from kafka import KafkaProducer

#kafka topic
ORDER_KAFKA_TOPIC = "order_details"

ORDER_LIMIT = 20_000

# write to kafka
producer = KafkaProducer(
# server where kafka is running
bootstrap_servers="localhost:29092"
)

# print("Going to be generating order after 5 seconds")
# print("Will generate one unique order every 5 seconds")

for i in range(1, ORDER_LIMIT):
    #simulate the data
    data = {
        "order_id" : 1,
        "user_id": f"tom_{i}",
        "total_cost": i * 2,
        "item": "burguer, sandwich"
    }
    # send data to producer
    producer.send(
        ORDER_KAFKA_TOPIC,
        #encode the data
        json.dumps(data).encode("utf-8")
    )
    print(f"Done sending..{i}")
    # time.sleep(5)