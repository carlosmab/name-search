from abc import ABC, abstractmethod
from typing import List
from app.models.search_result.search_result import SearchResult


class SearchEngine(ABC):

    @abstractmethod
    def get_search_results(self, keywords: list) -> List[SearchResult]: ...
    
    @abstractmethod
    def execute_query(self, query: list) -> List[SearchResult]: ...