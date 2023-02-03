Download the docker-compose image from bitname
curl -sSL https://raw.githubusercontent.com/bitnami/containers/main/bitnami/kafka/docker-compose.yml > docker-compose.yml

# Run the docker-compose file
docker-compose -f docker-compose.yml up

#Get container id
docker ps

# Execute container, with your container id
docker exec -it ba4373efeeae  bash

# Navigate into kafka folder
cd /opt/bitnami/kafka/bin/

#List topics
./kafka-topics.sh --list --bootstrap-server localhost:9092

#create topic
./kafka-topics.sh --create --topic my_topic --bootstrap-server localhost:9092

# run the producer
./kafka-console-producer.sh \
    --broker-list localhost:9092 \
    --topic my-topic

#on a new terminal, run the consumer
docker exec -it ba4373efeeae  bash

./kafka-console-consumer.sh \
    --bootstrap-server localhost:9092 \
    --topic my-topic \
    --from-beginning

# type messages on the producer terminal and check they're being consumed in the consumer terminal