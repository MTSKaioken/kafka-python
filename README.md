## Sobre o projeto.

A ideia é o modelo de negócio do projeto ser o mais simples possivel, para poder se concentrar na parte técnica.

Dito isso, ainda estou trabalhando no que os producers enviarão... pensei em ser algo em relação ao estoque, toda movimentação será enviada a uma fila que o producer irá capturar e enviar.
Sobre o consumer, irei somente capturar as mesmas movimentações as quais enviei e loga-las

Os endpoints criados utilizando o FastApi são para a possivel inclusão de um frontend que chamará este projeto.

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

## todo

- [ ] concluir a ideia do modelo de negócio do projeto...
- [ ] melhorar a arquitetura de módulos do projeto
- [ ] migrations para subir o esquema de collections no mongodb
- [ ] seeders para alimentar um pouco a collection.
- [ ] criar um middleware para controlar melhor a segurança na API
- [ ] retornar os status codes condizentes com o que será retornado
- [ ] criar um obj de retorno com os field padrões a serem retornados
 
- [x] parse DTO x Entidade