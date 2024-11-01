import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.internal.consumer import KafkaConsumer
from app.routes.websockets import router
from app.settings import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    kafka_consumer = KafkaConsumer()
    await kafka_consumer.start()
    broker = asyncio.ensure_future(kafka_consumer.exec())

    yield

    await kafka_consumer.stop()
    broker.cancel()


app = FastAPI(
    lifespan=lifespan,
    title=get_settings().server.project_description_api,
    version=get_settings().server.project_version_api,
    contact=get_settings().server.project_contact_api,
)

app.include_router(router)

templates = Jinja2Templates(directory='app/templates')
app.mount('/static', StaticFiles(directory='app/static'), name='app/static')


@app.get('/', response_class=HTMLResponse, description='Render the index.html template and start the WebSocket connection')
async def get(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
