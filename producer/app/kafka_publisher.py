import json
from fastapi import APIRouter, status
import os
import time
from confluent_kafka import Producer
from mongo_connection import get_con_db


router = APIRouter()
topic = os.getenv("TOPIC","my_topic")
bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS",'kafka:9092')



def get_data(page_num, batch_size=30):
    conn = get_con_db()
    skip_amount = page_num * batch_size
    cursor = conn.find().skip(skip_amount).limit(batch_size)
    return list(cursor)

def send_to_producer():
    page = 0
    while True:
        message = get_data(page)
        publish_message(message)
        if not message:
            break
        time.sleep(0.5)
        page += 1


def get_producer():
    p = Producer({'bootstrap.servers': bootstrap_servers})
    return p


def publish_message(message, topic=topic, producer=None):
    if not producer:
        producer = get_producer()
    try:
        json_data = json.dumps(message, default=str).encode('utf-8')
        producer.produce(topic, json_data)
        producer.flush()

    except Exception as e:
        print(f"Error publishing to Kafka: {e}")
