import json

from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
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


# @app.get("/RandomPal")
# async def root():
#     return await RandomPal()


@app.get("/Pal='{Pal}'")
async def root(Pal: str):
    await pal_info(Pal)

@app.get("/palIcon={Pal}")
async def root(Pal :str):
    await get_pal_icon(Pal)