import configparser
import mysql.connector
from mysql.connector import Error


def get_config():
    config = configparser.ConfigParser()
    config.read("..\\test.config.ini")
    return config


connect_config = {
    "host": get_config()['SQL']['host'],
    "database": get_config()['SQL']['database'],
    "user": get_config()['SQL']['user'],
    "password": get_config()['SQL']['password']
}


def get_db_connect():
    try:
        conn = mysql.connector.connect(**connect_config)

        if conn.is_connected():
            return conn
    except Error as e:
        print(e)



