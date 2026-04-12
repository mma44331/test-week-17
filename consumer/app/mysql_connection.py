import os
import mysql.connector



def get_mysql_conn():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "mysql"),
        user=os.getenv("MYSQL_USER", "user"),
        password=os.getenv("MYSQL_PASSWORD", "password"),
        database=os.getenv("MYSQL_DB", "my_analytics_db")
    )
#
# def get_mysql_conn():
#     attemps = 0
#     while attemps  < 10:
#         try:
#             conn = mysql.connector.connect(
#                 host=os.getenv("MYSQL_HOST", "mysql"),
#                 user=os.getenv("MYSQL_USER", "user"),
#                 password=os.getenv("MYSQL_PASSWORD", "password"),
#                 database=os.getenv("MYSQL_DB", "my_analytics_db")
#             )
#             return conn
#         except mysql.connector.Error as err:
#             attemps += 1
#             time.sleep(3)
#     raise Exception("Could not connect to MySQL after 10 attempts")
