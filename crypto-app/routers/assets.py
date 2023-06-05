import sys
import requests
import json
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request
from starlette import status
from starlette.responses import HTMLResponse, RedirectResponse
from routers.auth import get_current_user

sys.path.append("..")

routers = APIRouter(
    prefix="/assets",
    tags=["assets"],
    responses={404: {"description": "Not found"}}
)

templates = Jinja2Templates(directory="templates")


@routers.get('/', response_class=HTMLResponse)
async def get_all_assets(request: Request):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    # line for initialize API
    url = "https://api.coincap.io/v2/assets"

    payload = {}
    headers = {'Content-Type': 'application/json; charset=utf-8'}

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.text

    return templates.TemplateResponse("assets.html", {"request": request, "user": user, "data": data})


@routers.get('/{id}', response_class=HTMLResponse)
async def get_assets_by_id(request: Request):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    url = "https://api.coincap.io/v2/assets/" + id

    # line for initialize API
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.text

    return templates.TemplateResponse("assets.html", {"request": request, "user": user, "data": data})


@routers.get('/{id}/market', response_class=HTMLResponse)
async def get_assets_by_id(request: Request):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    url = "https://api.coincap.io/v2/assets/" + id + "/market"

    # line for initialize API
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.text

    return templates.TemplateResponse("assets.html", {"request": request, "user": user, "data": data})


@routers.get('/{id}/history', response_class=HTMLResponse)
async def get_assets_by_id(request: Request):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    url = "https://api.coincap.io/v2/assets/" + id + "/history"

    # line for initialize API
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.text

    return templates.TemplateResponse("assets.html", {"request": request, "user": user, "data": data})