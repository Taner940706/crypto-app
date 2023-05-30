import json
import sys
import urllib.request

from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import HTMLResponse, RedirectResponse
from database import SessionLocal
from routers.auth import get_current_user

sys.path.append("..")

routers = APIRouter(
    prefix="/assets",
    tags=["assets"],
    responses={404: {"description": "Not found"}}
)

templates = Jinja2Templates(directory="templates")


# session local for database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@routers.get('/', response_class=HTMLResponse)
async def get_all_assets(request: Request, db: Session = Depends(get_db)):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    # line for initialize API
    source = urllib.request.urlopen('https://api.coincap.io/v2/assets').open()
    data = json.loads(source)

    return templates.TemplateResponse("assets.html", {"request": request, "user": user, "data": data})


@routers.get('/{id}', response_class=HTMLResponse)
async def get_assets_by_id(request: Request, db: Session = Depends(get_db)):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    # line for initialize API
    source = urllib.request.urlopen('https://api.coincap.io/v2/assets'+{id}).open()
    data = json.loads(source)

    return templates.TemplateResponse("assets.html", {"request": request, "user": user, "data": data})


@routers.get('/{id}/market', response_class=HTMLResponse)
async def get_assets_by_id(request: Request, db: Session = Depends(get_db)):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    # line for initialize API
    source = urllib.request.urlopen('https://api.coincap.io/v2/assets' + {id} + "/market").open()
    data = json.loads(source)

    return templates.TemplateResponse("assets.html", {"request": request, "user": user, "data": data})


@routers.get('/{id}/history', response_class=HTMLResponse)
async def get_assets_by_id(request: Request, db: Session = Depends(get_db)):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    # line for initialize API
    source = urllib.request.urlopen('https://api.coincap.io/v2/assets' + {id} + "/history").open()
    data = json.loads(source)

    return templates.TemplateResponse("assets.html", {"request": request, "user": user, "data": data})