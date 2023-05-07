from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter

from database import SessionLocal

routers = APIRouter()
templates = Jinja2Templates(directory="templates")


# session local for database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()