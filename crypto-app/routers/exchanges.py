import sys
import json
import urllib.request
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates
from database import SessionLocal
from routers.auth import get_current_user

sys.path.append("..")

routers = APIRouter(
    prefix="/exchanges",
    tags=["exchanges"],
    responses={404: {"description": "Not found!"}}
)

templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@routers.get('/exchanges', response_class=HTMLResponse)
async def get_all_exchanges(request: Request, db: Session = Depends(get_db)):

    user = get_current_user(request)

    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    # line for initialize API
    source = urllib.request.urlopen('https://api.coincap.io/v2/assets' + "/history").open()
    data = json.loads(source)

    return templates.TemplateResponse('exchanges.html', {"request": request, "user": user, "data": data})


@routers.get('/exchanges/{id}', response_class=HTMLResponse)
async def get_exchanges_by_id(request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request)

    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    # line for initialize API
    source = urllib.request.urlopen('https://api.coincap.io/v2/assets' + {id} + "/history").open()
    data = json.loads(source)

    return templates.TemplateResponse('exchanges.html', {"request": request, "user": user, "data": data})