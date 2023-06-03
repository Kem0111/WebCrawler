from typing import Any, Optional, Tuple
from src.db.db_controller import DatabaseController
from src.db.sqlite_manager import SQLiteManager


def handle_database_interaction(query: str,
                                params: Optional[Tuple[Any]] = None):

    try:
        db_manager = SQLiteManager('db.sqlite3')
        controller = DatabaseController(db_manager)
        controller.execute_query(query, params)
    finally:
        controller.close_connection()
