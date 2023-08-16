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
    data = response.json()
    assets = data['data']

    return templates.TemplateResponse("assets/assets.html", {"request": request, "user": user, "assets": assets})


@routers.get('/{asset_id}', response_class=HTMLResponse)
async def get_assets_by_id(request: Request, asset_id: str):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    url = "https://api.coincap.io/v2/assets/" + asset_id

    # line for initialize API
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    assets = data['data']

    return templates.TemplateResponse("assets/get_asset_by_id.html", {"request": request, "user": user, "assets": assets})


@routers.get('/{asset_id}/market', response_class=HTMLResponse)
async def get_market_by_assets_by_id(request: Request, asset_id: str):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    url = "https://api.coincap.io/v2/assets/" + asset_id + "/markets"

    # line for initialize API
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    assets_market = data['data']

    return templates.TemplateResponse("assets/get_market_by_assets.html", {"request": request, "user": user, "assets_market": assets_market})


@routers.get('/{asset_id}/history', response_class=HTMLResponse)
async def get_assets_by_id(request: Request, asset_id: str):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    url = "https://api.coincap.io/v2/assets/" + asset_id + "/history?interval=" + "d1"
    url_asset = "https://api.coincap.io/v2/assets/" + asset_id

    # line for initialize API
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    response_asset = requests.request("GET", url_asset, headers=headers, data=payload)
    data = response.json()
    data_asset = response_asset.json()
    assets_history = data['data']
    asset = data_asset['data']
    print(assets_history)
    print(asset)

    return templates.TemplateResponse("assets/get_history_by_assets.html", {"request": request, "user": user, "assets_history": assets_history, "asset": asset})