import json
import random
import time
from kafka import KafkaProducer

#kafka topic
SHOPPING_ORDER_KAFKA_TOPIC = "shopping_order_details"

ORDER_LIMIT = 20_000

# write to kafka
producer = KafkaProducer(
# server where kafka is running
bootstrap_servers="localhost:29092"
)

print("Generating new shopping order after 5 seconds")

# List of country names
country_names = ["USA", "Canada", "Mexico", "Brazil", "Argentina", 
                 "Colombia", "Peru", "Venezuela", "Chile", "Ecuador"]

# List of item IDs
item_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Counter for unique IDs
user_id_counter = 1
order_id_counter = 1

while True:
    # Generate dictionary
    order = {
        "order_id": order_id_counter,
        "user_id": user_id_counter,
        "country_name": random.choice(country_names),
        "item_id": random.choice(item_ids),
        "item_price": random.uniform(10, 100),
        "email": f"{user_id_counter}@email.com",
        "card_status": random.choice(["approved", "denied"])
    }

    # send data to producer
    producer.send(
        SHOPPING_ORDER_KAFKA_TOPIC,
        #encode the data
        json.dumps(order).encode("utf-8")
    )
    print(order)
    print(f"Done sending order from user_id: {user_id_counter}")
     # Increase counters
    user_id_counter += 1
    order_id_counter += 1

    time.sleep(5)