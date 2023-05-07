from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter

routers = APIRouter()
templates = Jinja2Templates(directory="templates")