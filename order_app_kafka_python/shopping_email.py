from kafka import KafkaConsumer
import json

SHOPPING_ORDER_CONFIRMED_KAFKA_TOPIC = "shopping_order_confirmed"

consumer = KafkaConsumer(
SHOPPING_ORDER_CONFIRMED_KAFKA_TOPIC,
bootstrap_servers="localhost:29092"
)

print("Email is listening..")

while True:
    for message in consumer:
        consumed_message = json.loads(message.value.decode())
        customer_email = consumed_message["email"]
        order_id = consumed_message["order_id"]
        print(f"Sending email to {customer_email}, referring to order {order_id}")

        