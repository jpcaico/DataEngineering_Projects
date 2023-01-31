#read and write back to kafka
import json
from kafka import KafkaConsumer, KafkaProducer

SHOPPING_ORDER_KAFKA_TOPIC = "shopping_order_details"
SHOPPING_ORDER_CONFIRMED_KAFKA_TOPIC = "shopping_order_confirmed"

consumer = KafkaConsumer(

    SHOPPING_ORDER_KAFKA_TOPIC,
    bootstrap_servers = "localhost:29092"

)

producer = KafkaProducer(
    bootstrap_servers = "localhost:29092"
)

print("Shopping Transactions Listening..")
while True:
    for message in consumer:
        print("Ongoing Shopping transaction.. ")
        consumed_message = json.loads(message.value.decode())
        print(consumed_message)

        card_status = consumed_message["card_status"]
        # First check if the transaction was successfuly completed based on card status
        if card_status == "approved":

            # send confirmation to topic
            data = consumed_message
            print("Successful transaction, writing to topic")
            producer.send(SHOPPING_ORDER_CONFIRMED_KAFKA_TOPIC,
            json.dumps(data).encode("utf-8")
            )
        else:
            print("Order Denied, not writing to topic")


