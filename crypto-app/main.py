from fastapi import FastAPI, Depends
import models
from database import engine
from routers import crypto
from starlette.staticfiles import StaticFiles

app = FastAPI

models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(crypto.routers)