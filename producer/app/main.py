import json
import os
import time
from kafka_publisher import send_to_producer
from mongo_connection import get_con_db
file_path = os.getenv("DATA_FILE_PATH","suspicious_customers_orders.json")

conn = get_con_db()

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

if data is not None:
    conn.insert_many(data)
time.sleep(10)
send_to_producer()
