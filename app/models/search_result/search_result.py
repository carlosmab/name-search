from abc import ABC, abstractmethod
from pydantic import BaseModel


class SearchResult(ABC, BaseModel):
    title: str
    url: str
    snippet: str
    
    def __str__(self) -> str:
        return f"title: {self.title}, url: {self.url}, snippet: {self.snippet}"
    
    @abstractmethod
    def map_results(self, result: dict) -> None: ...
    
    
    