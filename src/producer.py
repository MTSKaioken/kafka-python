import json
from time import sleep

import requests
from confluent_kafka import Producer
import socket


def requestApi() -> str:
    response = requests.get(
        'https://api.open-meteo.com/v1/forecast',
        params={
            "latitude": 51.5,
            "longitude": -0.11,
            "current": "temperature_2m"

        },
    )
    return response.json()


conf = {'bootstrap.servers': 'localhost:9092,localhost:9092',
        'client.id': socket.gethostname()}
producer = Producer(conf)

while True:
    resposta = requestApi()
    producer.produce(topic="TESTE_KAFKA", key="London", value=json.dumps(resposta))
    sleep(10)
