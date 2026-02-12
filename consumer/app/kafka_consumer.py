import json
import os
from dotenv import load_dotenv
from datetime import datetime
from main import load_to_mysql
from confluent_kafka import Consumer, KafkaError

load_dotenv()

topic = os.getenv("TOPIC","my_topic")
bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS","localhost:9092")

def get_consumer(topic,group_id = "my_group",auto_offset_reset = "earliest"):
    consumer  = Consumer({
                  'bootstrap.servers': bootstrap_servers,
                  'group.id':group_id,
                  'auto.offset.reset': auto_offset_reset})
    consumer .subscribe([topic])
    return consumer

consumer = get_consumer(topic)
while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        if msg.error().code() != KafkaError._PARTITION_EOF:
            print("Consumer error:", msg.error())
        continue
    data = json.loads(msg.value().decode('utf-8'))
    load_to_mysql(data)
