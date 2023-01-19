import os

import pymysql


def mysql_execute(mysql_string):
    connection = mysql_connect()
    cursor = connection.cursor()
    cursor.execute(mysql_string)
    output = cursor.fetchall()
    connection.close()
    return output


def mysql_create_message_table():
    mysql_execute(
        "CREATE TABLE IF NOT EXISTS `messages` ( `server` TEXT, `channel` TEXT, `name` TEXT, `message` TEXT, "
        "`timestamp` DATE DEFAULT CURRENT_TIMESTAMP() )")


def mysql_check_table(table):
    return mysql_execute("show tables like '" + table + "'")


def mysql_connect():
    return pymysql.connect(
        host="corsolaa.ddns.net",
        user="hero_wars",
        passwd=os.getenv("DB-PASS"),
        database="hero_wars"
    )
