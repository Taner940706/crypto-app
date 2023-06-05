import sys
import requests
from fastapi import APIRouter, Request
from starlette import status
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates
from routers.auth import get_current_user

sys.path.append("..")

routers = APIRouter(
    prefix="/exchanges",
    tags=["exchanges"],
    responses={404: {"description": "Not found!"}}
)

templates = Jinja2Templates(directory="templates")


@routers.get('/', response_class=HTMLResponse)
async def get_all_exchanges(request: Request):

    user = get_current_user(request)

    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    url = "https://api.coincap.io/v2/exchanges"

    # line for initialize API
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.text

    return templates.TemplateResponse('exchanges.html', {"request": request, "user": user, "data": data})


@routers.get('/{id}', response_class=HTMLResponse)
async def get_exchanges_by_id(request: Request):
    user = get_current_user(request)

    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    url = "https://api.coincap.io/v2/exchanges/" + id

    # line for initialize API
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.text

    return templates.TemplateResponse('exchanges.html', {"request": request, "user": user, "data": data})