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
