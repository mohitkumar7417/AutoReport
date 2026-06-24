class DataSource:
    def read(self):
        raise NotImplementedError("Subclasses must implement read()")


class CSVDataSource(DataSource):
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        from autoreport.ingestion import read_csv
        return read_csv(self.file_path)

import pandas as pd
import sqlite3


class JSONDataSource(DataSource):
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        return pd.read_json(self.file_path)


class SQLiteDataSource(DataSource):
    def __init__(self, db_path, query):
        self.db_path = db_path
        self.query = query

    def read(self):
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query(self.query, conn)
        conn.close()
        return df
import pandas as pd
import sqlite3


class JSONDataSource(DataSource):
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        return pd.read_json(self.file_path)


class SQLiteDataSource(DataSource):
    def __init__(self, db_path, query):
        self.db_path = db_path
        self.query = query

    def read(self):
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query(self.query, conn)
        conn.close()
        return df