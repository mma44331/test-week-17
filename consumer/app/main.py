import os
import time
from datetime import datetime
import mysql.connector
from mysql_connection import get_mysql_conn


def load_to_mysql(data):
    conn = get_mysql_conn()
    cursor = conn.cursor()
    customers_to_insert = []
    orders_to_insert = []

    try:
        for item in data:
            item_type = item.get("type")

            if item_type == "customer":
                customer_data = (
                    item.get("customerNumber"),
                    item.get("customerName"),
                    item.get("contactLastName"),
                    item.get("contactFirstName"),
                    item.get("phone"),
                    item.get("city"),
                    item.get("country"),
                    item.get("creditLimit")
                )
                customers_to_insert.append(customer_data)

            elif item_type == "order":
                order_data = (
                    item.get("orderNumber"),
                    item.get("customerNumber"),
                    item.get("orderDate"),
                    item.get("status"),
                    item.get("comments")
                )
                orders_to_insert.append(order_data)

        if customers_to_insert:
            customer_query = """
                INSERT IGNORE INTO customers 
                (customerNumber, customerName, contactLastName, contactFirstName, phone, city, country, creditLimit)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.executemany(customer_query, customers_to_insert)

        if orders_to_insert:
            order_query = """
                INSERT IGNORE INTO orders 
                (orderNumber, customerNumber, orderDate, status, comments)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.executemany(order_query, orders_to_insert)

        conn.commit()
        print(f"Successfully processed {len(data)} items: "
              f"{len(customers_to_insert)} customers, {len(orders_to_insert)} orders.")

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        conn.rollback()
    except Exception as e:
        print(f"General Error: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()





