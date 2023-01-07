import os

import pymysql


def mysql_execute(mysql_string):
    connection = mysql_connect()
    cursor = connection.cursor()
    cursor.execute(mysql_string)
    output = cursor.fetchall()
    connection.close()
    return output


def mysql_connect():
    return pymysql.connect(
        host="corsolaa.ddns.net",
        user="hero_wars",
        passwd=os.getenv("DB-PASS"),
        database="hero_wars"
    )
