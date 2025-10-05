# Para rodar o nosso código, executar no terminal: [uvicorn main <- (nome do arquivo inicial o meu é main.py):app --reload]

from fastapi import FastAPI

app = FastAPI()
# Acima é a configuração padrão para rodar uma API no FASTAPI

# Para importar alguma outra classe ela tem que vim depois do comando inicial da aplicação,
# no caso, o código acima. Para evitar a referência circular.
from auth_routes import auth_routes
from order_routes import order_routes

# Pedindo para o app incluir as rotas que foram criadas
app.include_router(auth_routes)
app.include_router(order_routes)

