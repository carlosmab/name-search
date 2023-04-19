from unittest import TestCase
from app.models.search_result.google_search_result import GoogleSearchResult
from app.services.search_engines.google_search import GoogleSearchEngine


class GoogleSearchEngineTestCase(TestCase):
    def test_if_gse_service_is_available(self) -> None:
        words_to_search = ["test1", "test2", "test3"]
        found_web_pages = GoogleSearchEngine.get_search_results(words_to_search)  
        
        self.assertGreater(len(found_web_pages), 0)
        self.assertIsInstance(found_web_pages[0], GoogleSearchResult)
        