
from typing import Annotated, List

from fastapi import Body
from app.models.search_result.google_search_result import GoogleSearchResult
from app.models.search_result.search_result import EngineInfo, SearchResult
from app.routers.custom_api_router import CustomAPIRouter
from app.services.search_engines.google_search import GoogleSearchEngine


google_cse_router = CustomAPIRouter("google-cse")


@google_cse_router.get("/")
async def check_is_online() -> EngineInfo:
    return {
        "status": "ready",
        "provider": "google",
    } # type: ignore


@google_cse_router.post("/")
async def search_keywords(keywords: Annotated[list, Body(embed=True)] = []) -> List[GoogleSearchResult]:
    return GoogleSearchEngine.get_search_results(keywords)