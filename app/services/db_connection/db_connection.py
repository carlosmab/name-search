from abc import ABC, abstractmethod
from typing import Optional


class DBConnection(ABC):
    
    @abstractmethod
    def connect(self) -> None: ...
    
    @abstractmethod
    def execute_query(self, query: str) -> Optional[list]: ...
     
    @abstractmethod
    def close(self) -> None: ...
        
    @abstractmethod
    def set_params_from_env(self) -> None: ...