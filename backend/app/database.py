import mysql.connector
from app import config

def get_conn():
    return mysql.connector.connect(
        host=config.STARROCKS_HOST,
        port=config.STARROCKS_PORT,
        user=config.STARROCKS_USER,
        password=config.STARROCKS_PASS,
        database=config.STARROCKS_DB
    )
