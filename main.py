import os
from contextlib import asynccontextmanager
from datetime import datetime

import uvicorn
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
from fastapi import FastAPI

from src.middlewares.rate_limiter_middleware import RateLimiterMiddleware
from src.routes import product_route


def load_environment():
    if os.path.isfile('.env'):
        load_dotenv('.env')
    elif os.path.isfile('.env.dev'):
        load_dotenv('.env.dev')
    else:
        raise RuntimeError("Defina as variaveis do projeto no .env")


load_environment()

def do_work():
    print(f'{datetime.now()} executando job')

@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.add_job(do_work, "interval", seconds=5)
    scheduler.start()
    print('subiu')
    yield
    print('terminou de subir')


app = FastAPI(lifespan=lifespan)
scheduler = BackgroundScheduler()

app.add_middleware(RateLimiterMiddleware)
app.include_router(product_route.router)

URL_HOST_PROJECT = os.getenv('URL_HOST_PROJECT')
URL_PORT_PROJECT = os.getenv('URL_PORT_PROJECT')
uvicorn.run(app, host=URL_HOST_PROJECT, port=int(URL_PORT_PROJECT))
