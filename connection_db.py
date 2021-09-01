import sqlite3
from sqlite3.dbapi2 import connect

def connect_db():
    conn = sqlite3.connect("bank.db")
    c = conn.cursor()
    return conn, c

def create_table():
    conn, c = connect_db()
    # SQL SYNTAX
    CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS BANK_DETAILS(
    NAME VARCHAR(50),
    PHONE VARCHAR(13),
    EMAIL VARCHAR(50),
    ADDRESS VARCHAR(100),
    ACC_TYPE VARCHAR(50),
    ACC_NUMBER VARCHAR(50),
    USER_ID VARCHAR(50),
    PIN INTEGER(4),
    BALANCE VARCHAR(400)
    );
    """
    c.execute(CREATE_TABLE)

create_table()