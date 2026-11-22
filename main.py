from utilities.packet_util import packet_import
packet_import(["sqlite3", "argon2-cffi", "psycopg2-binary"])

from utilities.sqlite_util import DB
from utilities.postgre_util import THOTH
from utilities.cli_util import CLI

db = THOTH()

db.create_table("users", {"id": "INTEGER PRIMARY KEY", "name": "TEXT", "age": "INTEGER"})
db.close()
