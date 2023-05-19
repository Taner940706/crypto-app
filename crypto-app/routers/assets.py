from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import HTMLResponse, RedirectResponse

from database import SessionLocal
from routers.auth import get_current_user

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


@routers.get('/assets', response_class=HTMLResponse)
async def get_all_assets(request: Request, db: Session = Depends(get_db)):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    # line for initialize API

    return templates.TemplateResponse("assets.html", {"request": request, "user": user})


@routers.get('assets/{id}', response_class=HTMLResponse)
async def get_assets_by_id(request: Request, db: Session = Depends(get_db)):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    # line for initialize API

    return templates.TemplateResponse("assets.html", {"request": request, "user": user})


@routers.get('assets/{id}/market', response_class=HTMLResponse)
async def get_assets_by_id(request: Request, db: Session = Depends(get_db)):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    # line for initialize API

    return templates.TemplateResponse("assets.html", {"request": request, "user": user})


@routers.get('assets/{id}/history', response_class=HTMLResponse)
async def get_assets_by_id(request: Request, db: Session = Depends(get_db)):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    # line for initialize API

    return templates.TemplateResponse("assets.html", {"request": request, "user": user})