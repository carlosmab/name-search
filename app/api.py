from fastapi import FastAPI
from app.routers.custom_search.custom_search_router import custom_search_router
from app.routers.auth.auth_router import auth_router
from app.routers.name_extraction.name_extraction_router import name_extraction_router



app = FastAPI()

app.include_router(auth_router)
app.include_router(custom_search_router)
app.include_router(name_extraction_router)


@app.get('/')
async def welcome():
    return {
        "title": "Name Search API",
        "description": "Name extraction from pdf files and custom web search",
    }
