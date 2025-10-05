from fastapi import APIRouter

order_routes = APIRouter(prefix="/order", tags=["orders"])
# Indica que esta classe é uma classe de routes
# Já o prefix indica que o path dessa route sempre começará com /order, por exemplo: /order/id
# Já o tags, é para criar uma seção no SWAGGER somente para essa rota, mais questão de organização, é passada como lista pois pode definir mais de uma tag

@order_routes.get("/")  # Decorator que indica que requisição essa rota vai utilizar, bem parecido com o spring
async def get_all_orders():
    return {
        "mensagem": "Você acessou a rota de pedidos"
    } # Retorna um JSON com a mensagem acima, deixei em estilo JSON para facilidade de entendimento

