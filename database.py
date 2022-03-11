"""
Module contains the database settings
ALL RIGHTS RESERVED
COPYRIGHT (C) 2021
BRAHIM RABEB
"""
import mysql.connector


##################################################################
# function to use for connection and sending data to the database
##################################################################

def write_to_db(sqlstatement):
    """
    Write to mySql in phpMyAdmin
    """
    try:
        print(sqlstatement)
        conn = mysql.connector.connect(
            user="rabeb",
            password="rabeb",
            host="localhost",
            port="8889",
            database="system_analyser"
        )
    except mysql.connector.Error as e:
        print(f"Error connecting to mySql Platform: {e}")
        return

    cur = conn.cursor()

    cur.execute(sqlstatement)

    conn.commit()

    conn.close()
