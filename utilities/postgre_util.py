import psycopg2
import getpass
from typing import Literal

class THOTH:
    # Transactional Handler for Operational Table Handling: T.H.O.T.H
    def __init__(self):
        self.input_prefix = "T.H.O.T.H"
        self.__conn = self.connect()
        self.__commit = lambda: self.__conn.commit()
        self.__close = lambda: self.__conn.close()

    def _d_type_checker(self, value, expected_type: Literal["str", "int", "float", "bool"]):
        match value:
            case str() if expected_type == "str":
                return True
            case int() if expected_type == "int":
                return True
            case float() if expected_type == "float":
                return True
            case bool() if expected_type == "bool":
                return True
            case _:
                return False

    def connect(self):
        while True:
            username = input(f"{self.input_prefix}> username:\n>>> ")
            if not self._d_type_checker(username, "str"):
                continue
            password = getpass.getpass(f"{self.input_prefix}> password:\n>>> ")
            if not self._d_type_checker(password, "str"):
                continue
            host = input(f"{self.input_prefix}> host:\n>>> ")
            if not self._d_type_checker(host, "str"):
                continue
            port = input(f"{self.input_prefix}> port:\n>>> ")
            if not self._d_type_checker(port, "str"):
                continue
            database = input(f"{self.input_prefix}> database:\n>>> ")
            if not self._d_type_checker(database, "str"):
                continue
            conn = psycopg2.connect(
                user=username,
                password=password,
                host=host,
                port=port,
                database=database
            )
            self.input_prefix = f"T.H.O.T.H/{username}@{host}:{port}"
            return conn

    # CREATE

    def create_table(self, table_name:str, columns: dict):
        column_defs = ", ".join([f"{col} {dtype}" for col, dtype in columns.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_defs});"
        with self.__conn.cursor() as cursor:
            cursor.execute(query)
            self.__commit()
        return self

    def add_data(self, table_name, data: dict, params: list):
        columns = ", ".join(data.keys())
        values = ", ".join(["%s"] * len(data))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
        with self.__conn.cursor() as cursor:
            cursor.execute(query, params)
            self.__commit()
        return self

    # READ

    def get_data(self, table_name, columns: list, condition: str, params: list):
        cols = ", ".join(columns) if columns else "*"
        query = f"SELECT {cols} FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        query += ";"
        with self.__conn.cursor() as cursor:
            cursor.execute(query, params or [])
            result = cursor.fetchall()
        return result

    # UPDATE

    def update_data(self, table_name, data: dict, condition: str, params: list):
        set_clause = ", ".join([f"{col} = %s" for col in data.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition};"
        with self.__conn.cursor() as cursor:
            cursor.execute(query, params)
            self.__commit()
        return self

    # DELETE

    def delete_data(self, table_name, condition: str, params: list):
        query = f"DELETE FROM {table_name} WHERE {condition};"
        with self.__conn.cursor() as cursor:
            cursor.execute(query, params)
            self.__commit()
        return self
    
    def close(self):
        self.__close()

