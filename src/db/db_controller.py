from typing import Any, List, Optional

from src.db.abstact_db_manager import AbstractDatabaseManager


class DatabaseController:

    def __init__(self, manager: AbstractDatabaseManager):
        self.manager = manager

    def execute_query(self, query: str, params: Optional[List[Any]] = None):
        try:
            return self.manager.execute_query(query, params)
        except Exception as e:
            print(f"An error occurred: {e}")

    def close_connection(self):
        self.manager.close()
