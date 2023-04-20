from fastapi import FastAPI
from app.routers.custom_search.custom_search_router import custom_search_router

app = FastAPI()

app.include_router(custom_search_router)

@app.get('/')
async def welcome():
    return {
        "title": "Name Search API",
        "description": "Name extraction from pdf files and custom web search",
    }
