import sqlite3
from sqlalchemy import create_engine
import pandas as pd
import pymysql
import os


conn = sqlite3.connect("./Database/strive.db")


def get_conn():
    try:
        conn = sqlite3.connect("./Database/strive.db")
        return conn
    except Exception as ex:
        print(ex)
        return ex


def get_remote_conn(user, pas, IP, port):
    try:
        engine = create_engine(
            f'mysql+pymysql://{user}:{pas}@{IP}/{user}?host={IP}?port={port}')
        conn = engine.connect
        return conn
    except Exception as ex:
        print(ex)
        return ex


def sql_execute(sentence):

    try:
        c = conn.cursor()
        a = c.execute(sentence)
        conn.commit()
        print(a)
    except Exception as ex:
        print(ex)
        return ex


def pd_upload_csv(name: str, pth, head=0):
    try:
        df = pd.read_csv(pth, header=head)
        frame = df.to_sql(name, get_conn(), if_exists='replace', index=False)
        return frame
    except Exception as ex:
        print(ex)
        return ex


def pandas_select(stc):
    try:
        if stc.split()[0].lower() == "select":
            df = pd.read_sql_query(stc, conn)
            return df
        else:
            return pd.DataFrame()
    except Exception as ex:
        return pd.DataFrame()


def sql_query(stc):
    try:
        c = conn.cursor()
        reply = c.execute(stc)
        conn.commit()
        return reply
    except Exception as ex:
        print(ex)


def close():
    conn.close()
