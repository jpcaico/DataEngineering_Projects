Here is a detailed guide to execute the steps to build a data pipeline that reads a stock market data from a CSV file in Python, pipes it into S3, Glue, and Athena through a Kafka instance in EC2, written in markdown format:

# 1. Launching EC2 Instance
1. Go to EC2
2. Click on "Launch an Instance"
3. Keep default options and free tiers
4. Create a key pair to connect to the local machine (RSA and .pem file)
5. Put the .pem file in your project folder
6. Launch the instance
# 2. Connecting to EC2 Instance
After the instance is running, click on the instance ID and connect
1. Copy the ssh command
2. Go to the project folder where you have the .pem file and run the command:
```
chmod 400 kafka-stock-analysis.pem
ssh -i "kafka-stock-analysis.pem" ec2-user@ec2-52-3-254-234.compute-1.amazonaws.com
```

# 3. Installing Apache Kafka
1. Download Apache Kafka
`wget https://downloads.apache.org/kafka/3.3.2/kafka_2.12-3.3.2.tgz`

2. Uncompress the file
`tar -xvf kafka_2.12-3.3.2.tgz`

3. Install Java Virtual Machine (JVM)
`sudo yum install java-1.8.0-openjdk`
`java -version`

## Start Zookeeper

```cd kafka_2.12-3.3.2/
bin/zookeeper-server-start.sh config/zookeeper.properties
```


# 4. Starting Kafka Server
1. Open another terminal and connect to the instance again
2. Increase memory for the Kafka server

`export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"`

3. Start the Kafka server
`bin/kafka-server-start.sh config/server.properties`

# 5. Configuring Server.properties
1. Change server.properties file to run in public IPv4
`sudo nano config/server.properties`
Replace the line
```#advertised.listeners=PLAINTEXT://your.host.name:9092```
with
```
advertised.listener=PLAINTEXT://<your_public_ipv4_address>:9092
advertised.listeners=PLAINTEXT://52.3.254.234:9092
```

# 6. Allowing Requests from Local Machine to EC2 Instance
1. On the EC2 console, click on Security
2. Click on Security Groups
3. Edit inbound rules
4. Add "All Traffic" and "Anywhere IPv4" (or "My IP")
5. Save it (Note: this is not the best practice)

# 7. Creating Topics and Starting Producers and Consumers
1. Open a new terminal and connect to the EC2 machine again
2. Create the topic
```
bin/kafka-topics.sh --create --topic demo_test --bootstrap-server {Put the Public IP of your EC2 Instance:9092} --replication-factor 1 --partitions 1
bin/kafka-topics.sh --create --topic demo_test --bootstrap-server 52.3.254.234:9092 --replication-factor 1 --partitions 1
```
3. Start the producer
```
bin/kafka-console-producer.sh --topic demo_test --bootstrap-server {Put the Public IP of your EC2 Instance:9092}
bin/kafka-console-producer.sh --topic demo_test --bootstrap-server 52.3.254.234:9092
```
4. Open new terminal
5 .Start the consumer
```
bin/kafka-console-consumer.sh --topic demo_test --bootstrap-server {Put the Public IP of your EC2 Instance:9092}
bin/kafka-console-consumer.sh --topic demo_test --bootstrap-server 52.3.254.234:9092
```

# 8. Creating producer in python
Follow files `KafkaProducer.py` and `KafkaConsumer.py`

# 9. Create a s3 bucket
My example runs on `stock-analysis-jpcaico`. You can use the configuration you want for the bucket, I just used default.

# 10. Install s3fs package
`python -m pip install s3fs`

# 11. Generate User Access Keys
1.  Go to IAM and create a new user and add access key
2. Download aws cli
3. config environment running int terminal
`aws configure`
4. Enter your  access key id and secret and region

# 12. Create Crawler
Create crawler in console, point it to the bucket where data will be stored.

Now data is being piped to Athena, dont forget to add a bucket for athena to save files
