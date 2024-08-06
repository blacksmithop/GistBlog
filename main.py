from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gist_wrapper import Gist

app = FastAPI()

VERSION = "0.0.1-preview"


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

gist = Gist()


@app.get("/")
async def index():
    return {"version": VERSION}


@app.get("/get_gists")
async def get_gists():
    return gist.get.get_gists()