from app.routers.custom_api_router import CustomAPIRouter
from app.routers.custom_search.google_cse.google_cse_router import google_cse_router

custom_search_router = CustomAPIRouter("custom-search")
custom_search_router.include_router(google_cse_router)

@custom_search_router.get("/")
async def custom_search_root():
    return "custom search"