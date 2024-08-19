import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from src.routes import product_route


def load_environment():
    if os.path.isfile('.env'):
        load_dotenv('.env')
    elif os.path.isfile('.env.dev'):
        load_dotenv('.env.dev')
    else:
        raise RuntimeError("Defina as variaveis do projeto no .env")


load_environment()
app = FastAPI()
app.include_router(product_route.router)

URL_HOST_PROJECT = os.getenv('URL_HOST_PROJECT')
URL_PORT_PROJECT = os.getenv('URL_PORT_PROJECT')
uvicorn.run(app, host=URL_HOST_PROJECT, port=int(URL_PORT_PROJECT))