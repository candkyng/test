import configparser
import mysql.connector
from mysql.connector import Error


def get_config():
    config = configparser.ConfigParser()
    config.read("..\\test.config.ini")
    return config


connect_config = {
    "host": get_config()['SQL']['host'],
    "user": get_config()['SQL']['user'],
    "password": get_config()['SQL']['password']
}


def get_mysql_connect():
    try:
        conn = mysql.connector.connect(**connect_config)

        if conn.is_connected():
            return conn
    except Error as e:
        print(e)


def run_sql_script(file):
    conn = get_mysql_connect()
    try:
        cursor = conn.cursor()
        f = open(file)
        lines = f.readlines()
        for line in lines:
            cursor.execute(line)
        conn.commit()
        conn.close()
    except Error as e:
        print(e)


def run_sql_query(query, data=None):

    conn = get_mysql_connect()
    try:
        cursor = conn.cursor()
        cursor.execute(query, data)
        result_all = cursor.fetchall()
        conn.commit()
        conn.close()
        return result_all
    except Error as e:
        print(e)



run_sql_script("..\\data\\pet_data.sql")
print(run_sql_query("Select * from petstore.pets; "))