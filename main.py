import json

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from routes.pal_info import pal_info
from routes.pal_icon import get_pal_icon
from utils.random_pal import RandomPal

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)


@app.get("/PalList")
async def root():
    return FileResponse("./PalList.json")


@app.get("/randomPal")
async def root():
    return await RandomPal()


@app.get("/Pal='{Pal}'")
async def root(Pal: str, request: Request):
    await pal_info(Pal, request)


@app.get("/palIcon={Pal}")
async def root(Pal: str):
    return await get_pal_icon(Pal)
