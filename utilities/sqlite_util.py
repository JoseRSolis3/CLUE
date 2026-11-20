import sqlite3
import os 
from argon2 import PasswordHasher

class DB:
    def __init__(self, db_name:str):
        self.__name = db_name
        self._check()

    def encrypt_password(self, password:str) -> str:
        ph = PasswordHasher()
        return ph.hash(password)

    def verify_password(self, hashed_password:str, password:str) -> bool:
        ph = PasswordHasher()
        try:
            ph.verify(hashed_password, password)
            return True
        except Exception as e:
            return False

    def _check(self):
        folder = "databases"
        match self.__name:
            case x if x.endswith('.db'):
                conn = sqlite3.connect(os.path.join(folder, self.__name))
            case x if not x.endswith('.db'):
                x += '.db'
                conn = sqlite3.connect(os.path.join(folder, x))
        conn.close()
        return self

    def add_data(self, table_name:str, data:dict):
        conn = sqlite3.connect(os.path.join("databases", self.__name))
        cursor = conn.cursor()
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        values = tuple(data.values())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cursor.execute(query, values)
        conn.commit()
        conn.close()

    def create_table(self, table_name:str, columns:dict):
        conn = sqlite3.connect(os.path.join("databases", self.__name))
        cursor = conn.cursor()
        columns_def = ', '.join([f"{col} {dtype}" for col, dtype in columns.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_def})"
        cursor.execute(query)
        conn.commit()
        conn.close()

    def get_data(self, table_name:str, conditions:dict):
        conn = sqlite3.connect(os.path.join("databases", self.__name))
        cursor = conn.cursor()
        query = f"SELECT * FROM {table_name}"
        if conditions:
            cond_str = ' AND '.join([f"{col} = ?" for col in conditions.keys()])
            query += f" WHERE {cond_str}"
            cursor.execute(query, tuple(conditions.values()))
        else:
            cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return rows

test = DB("test.db")
pw = test.encrypt_password("my_password")
print(test.verify_password(pw, "my_password"))
print(test.verify_password(pw, "wrong_password"))
