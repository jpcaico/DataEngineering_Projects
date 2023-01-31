from kafka import KafkaConsumer
import avro.schema
from avro.io import DatumReader, BinaryDecoder
import io
import os
import json
import boto3

# s3 configuration
# Get access key and secret key from environment variables
access_key = os.environ.get('AWS_ACCESS_KEY_ID')
secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

# Create a session using the environmental variables
session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)

# Create a S3 client
s3 = session.client('s3')

# Load the Avro schema
schema = avro.schema.Parse(open("./schema.avsc", "rb").read())

# Create a DatumReader
reader = DatumReader(schema)

def decode(msg_value):
    message_bytes = io.BytesIO(msg_value)
    message_bytes.seek(7)
    decoder = BinaryDecoder(message_bytes)
    event_dict = reader.read(decoder)
    return event_dict

# configure the Kafka consumer
consumer = KafkaConsumer("postgres.public.ingredients",
                        bootstrap_servers=["localhost:29092"])

print(consumer.bootstrap_connected())
print(consumer.subscription())

# Continuously poll for new messages
print("Listening..")
while True:
    count = 0
    for msg in consumer:
        data = decode(msg.value)
        print(data)

        print("Saving it to s3 bucket..")
        # Save the dictionary to a JSON file
        json_file = 'data.json'
        with open(json_file, 'w') as f:
            json.dump(data, f)

        # Upload the JSON file to S3
        s3.upload_file(json_file, 'your-bucket-name', f'your-object-key_{count}')
        count += 1
