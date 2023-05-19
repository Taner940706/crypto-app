from fastapi import FastAPI, Depends
import models
from database import engine
from routers import assets, exchanges, markets, rates, auth
from fastapi.staticfiles import StaticFiles


app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(assets.routers)
app.include_router(auth.routers)
app.include_router(exchanges.routers)
app.include_router(markets.routers)
app.include_router(rates.routers)