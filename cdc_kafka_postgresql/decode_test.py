from kafka import KafkaConsumer
import avro.schema
from avro.io import DatumReader, BinaryDecoder
import io
import logging
import json

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

data = decode(b'\x00\x00\x00\x00\x02\x00\x02*\x10moacyrlo\x06\x161.4.2.Final\x14postgresql\x10postgres\xa2\x8b\xd6\xf4\xbfa\x00\nfalse\x08food\x0cpublic\x16ingredients\x02\xf0\x07\x02\xf0\x8e\xe7\x16\x00\x02c\x02\xec\x90\xd6\xf4\xbfa\x00')
print(data)