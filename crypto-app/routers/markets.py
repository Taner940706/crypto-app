import sys
import json
import requests
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates
from database import SessionLocal
from routers.auth import get_current_user

sys.path.append("..")

routers = APIRouter(
    prefix="/markets",
    tags=["markets"],
    responses={404: {"description": "Not found!"}}
)

templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@routers.get("/", response_class=HTMLResponse)
async def get_all_markets(request: Request, db: Session = Depends(get_db)):

    user = get_current_user(request)

    if user is None:
        return RedirectResponse('/auth', status_code=status.HTTP_302_FOUND)

    url = 'https://api.coincap.io/v2/markets'

    # line for initialize API
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    markets = data['data']

    return templates.TemplateResponse('markets/markets.html', {"request": request, "user": user, "markets": markets})