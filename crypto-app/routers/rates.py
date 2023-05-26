import sys
import json
import urllib.request
from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates
from database import SessionLocal
from routers.auth import get_current_user

sys.path.append("..")

routers = APIRouter(
    prefix="/rates",
    tags=["rates"],
    responses={404: {"description": "Not found!"}}
)


templates = Jinja2Templates(directory="templates")


# session local for database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@routers.get('/rates', response_class=HTMLResponse)
async def get_all_rates(request: Request, db: Session = Depends(get_db)):

    user = get_current_user(request)

    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    # line for initialize API
    source = urllib.request.urlopen('https://api.coincap.io/v2/rates').open()
    data = json.loads(source)

    return templates.TemplateResponse('rates.html', {"request": request, "user": user, "data": data})


@routers.get('/rates/{id}', response_class=HTMLResponse)
async def get_rates_by_id(request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request)

    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    # line for initialize API
    source = urllib.request.urlopen('https://api.coincap.io/v2/rates' + {id}).open()
    data = json.loads(source)

    return templates.TemplateResponse('rates.html', {"request": request, "user": user, "data": data})
