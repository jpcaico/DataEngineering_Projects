from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers='kafka:9092')
topics = consumer.topics()
print("Topics available for connection:", topics)