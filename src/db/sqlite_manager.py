import sqlite3
from typing import Any, Optional, Tuple
from src.db.abstact_db_manager import AbstractDatabaseManager


class SQLiteManager(AbstractDatabaseManager):
    def __init__(self, db: str):
        self.conn = sqlite3.connect(db)

    def execute_query(self, query: str, params: Optional[Tuple[Any]] = None):
        with self.conn:
            cur = self.conn.cursor()
            if params:
                cur.execute(query, params)
            else:
                cur.execute(query)
            return cur.fetchall()

    def close(self):
        self.conn.close()
