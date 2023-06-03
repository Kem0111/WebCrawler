from abc import ABC, abstractmethod
from typing import List, Any, Optional


class AbstractDatabaseManager(ABC):
    @abstractmethod
    def execute_query(self, query: str, params: Optional[List[Any]] = None):
        pass

    @abstractmethod
    def close(self):
        pass
