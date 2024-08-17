## pre-requisitos
- poetry 1.8.3
- python >=3.8

````bash
git clone git@github.com:MTSKaioken/kafka-python.git
````

para instalar as dependências usadas no projeto
```bash
poetry install
```

Para rodar o software na porta 8000
```bash 
 uvicorn src.main:app 
```