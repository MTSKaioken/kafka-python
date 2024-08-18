import schedule
from datetime import datetime
import requests
def minha_tarefa():
    print(f'{datetime.now()} - Executando tarefas...')
    response = requests.get('https://viacep.com.br/ws/01001000/json/')
    if response.status_code == 200:
        # Processar a resposta
        data = response.json()  # ou response.text se não for JSON
        print(data)
    else:
        print(f"Erro {response.status_code}: {response.text}")


# Agendar a tarefa para ser executada a cada minuto
schedule.every(1).minute.do(minha_tarefa)

# Executar o cronjob indefinidamente
while True:
    schedule.run_pending()