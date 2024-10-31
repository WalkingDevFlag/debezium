import json


from fastapi.responses import HTMLResponse
import asyncio

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi import Request

from routes.websockets import router, consume_kafka



app = FastAPI()

app.include_router(router)

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="app/static")

@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.on_event("startup")
async def startup_event():
    asyncio.create_task(consume_kafka())
