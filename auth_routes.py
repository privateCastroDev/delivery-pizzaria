from fastapi import APIRouter

auth_routes = APIRouter(prefix="/auth", tags=["auth"])
# Indica que esta classe é uma classe de routes
# Já o prefix indica que o path dessa route sempre começará com /auth, por exemplo: /auth/refresh
# Já o tags, é para criar uma seção no SWAGG somente para essa rota, mais questão de organização

@auth_routes.get("/") # Decorator que indica que requisição essa rota vai utilizar, bem parecido com o spring
async def get_all_auths():
    return {
        "mensagem": "Você acessou a rota de auths",
        "autenticado": False
    } # Retorna um JSON com a mensagem acima, deixei em estilo JSON para facilidade de entendimento

