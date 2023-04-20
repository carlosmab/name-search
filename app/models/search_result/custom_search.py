from datetime import date
from typing import List
from pydantic import BaseModel

from app.models.search_result.search_result import SearchResult


class CustomSearch(BaseModel):
    search_by: int = 0
    result_records: int = 0
    date_search: date
    engine: int = 0
    records: List[SearchResult] = []
    

class CustomSearchRecord(BaseModel):
    record: SearchResult
    
    