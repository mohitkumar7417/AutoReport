import pandas as pd


def read_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading CSV: {e}")


def read_excel(file_path):
    try:
        return pd.read_excel(file_path)
    except Exception as e:
        print(f"Error reading Excel: {e}")

import json


def read_json(file_path):
    return json.load(open(file_path, "r"))


import sqlite3
import pandas as pd


def read_sqlite(db_path, table_name):
    conn = sqlite3.connect(db_path)

    df = pd.read_sql_query(
        f"SELECT * FROM {table_name}",
        conn
    )

    conn.close()

    return df