from app.models.search_result.search_result import SearchResult


class GoogleSearchResult(SearchResult):
    """
        Pydantic Model for Google Custom Search Engine Results
    """
    
    @staticmethod
    def map_results(result: dict) -> "GoogleSearchResult":
        return GoogleSearchResult(
            title=result["title"],
            url=result["link"],
            snippet=result["snippet"]
        )