from unittest import TestCase


class GSETestCase(TestCase):
    def test_if_gse_service_is_available(self) -> None:
        words_to_search = ["test1", "test2", "test3"]
        found_web_pages = GSE.search_words(words_to_search)
        assert len(found_web_pages) > 0
        