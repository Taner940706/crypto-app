import sys
import requests
from fastapi import APIRouter, Request
from starlette import status
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates
from routers.auth import get_current_user

sys.path.append("..")

routers = APIRouter(
    prefix="/rates",
    tags=["rates"],
    responses={404: {"description": "Not found!"}}
)


templates = Jinja2Templates(directory="templates")


@routers.get('/', response_class=HTMLResponse)
async def get_all_rates(request: Request):

    user = get_current_user(request)

    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    url = 'https://api.coincap.io/v2/rates'

    # line for initialize API
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    rates = data['data']

    return templates.TemplateResponse('rates.html', {"request": request, "user": user, "rates": rates})


@routers.get('/{rate_id}', response_class=HTMLResponse)
async def get_rates_by_id(request: Request, rate_id: str):
    user = get_current_user(request)

    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    # line for initialize API
    url = 'https://api.coincap.io/v2/rates/' + rate_id

    # line for initialize API
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    rate = data['data']

    return templates.TemplateResponse('get_rates_by_id.html', {"request": request, "user": user, "rate": rate})
