import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from app.services.search_engines.search_engine import SearchEngine
from app.models.search_result.google_search_result import GoogleSearchResult
from typing import List


load_dotenv()


class GoogleSearchEngine(SearchEngine):
    """
        Search engine service for consuming Google Custom Search API
    """
    
    results_per_page: int = 10 
    start_index: int = 1  
    
    @staticmethod
    def get_search_results(keywords: list) -> List[GoogleSearchResult]:
        query = " or ".join(keywords)    
        return GoogleSearchEngine.execute_query(query)
        
    @staticmethod
    def execute_query(query: str) -> List[GoogleSearchResult]:
        api_key: str = os.environ.get("CSE_API_KEY", "")
        cse_id: str = os.environ.get("CSE_ID", "")
        service = build('customsearch', 'v1', developerKey=api_key)
        result = service.cse().list(
            q=query,
            cx=cse_id,
            num=GoogleSearchEngine.results_per_page,
            start=GoogleSearchEngine.start_index
        ).execute()    
        return [GoogleSearchResult.map_results(item) for item in result["items"]]
    
    

