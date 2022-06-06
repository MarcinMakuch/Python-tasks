from fastapi import FastAPI

from GetInfo import get_statistics

app = FastAPI()


@app.get("/")
async def root(url: str):
    stats = get_statistics(url)
    return stats

# 'https://pl.wikipedia.org/wiki/Iga_%C5%9Awi%C4%85tek
