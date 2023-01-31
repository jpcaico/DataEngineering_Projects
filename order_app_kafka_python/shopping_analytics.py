import json
from google.cloud import bigquery
from kafka import KafkaConsumer
import os
import pandas as pd
from pandas_gbq import gbq
# Service account JSON key file path
key_file_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

# Create BigQuery client
client = bigquery.Client.from_service_account_json(key_file_path)


# BigQuery dataset and table name
project_id = "data-eng-bootcamp-375819"
dataset_id = "orders_dataset"
table_id = "orders_table"


SHOPPING_ORDER_CONFIRMED_KAFKA_TOPIC = "shopping_order_confirmed"

consumer = KafkaConsumer(
    SHOPPING_ORDER_CONFIRMED_KAFKA_TOPIC, 
    bootstrap_servers="localhost:29092"
)

total_orders_count = 0
total_revenue = 0

print("Listening to confirmed transactions..")
while True:
    for message in consumer:

        print("Updating analytics..")

        consumed_message = json.loads(message.value.decode())

        total_cost = float(consumed_message["item_price"])
        total_orders_count += 1
        total_revenue += total_cost

        print(f"Orders so far today: {total_orders_count}")
        print(f"Revenue so far today: {total_revenue}")
        print(f"Sending data to table in BigQuery")

        # Insert data into the table
        # Convert data to a Pandas DataFrame
        df = pd.DataFrame([consumed_message], columns=consumed_message.keys())
        df = df.astype({"order_id": int, "user_id": int, "country_name": str, "item_id": str, "item_price": float, "email": str, "card_status": str})
        gbq.to_gbq(df, f"{dataset_id}.{table_id}", project_id=project_id, if_exists="append")

        print("Order successfully sent to table in BigQuery!")

