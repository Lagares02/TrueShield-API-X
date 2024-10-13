from fastapi import APIRouter
from models.models import RequestModel, ResponseModel
from services.x import search_tweets

router = APIRouter()

@router.get("/")
async def home():
    return {"message": "Bienvenido!"}

@router.post("/contrasting_x", response_model=ResponseModel)
async def contrasting(request: RequestModel):
    # Extraer las palabras clave de la solicitud
    Keywords = request.keywords + request.subjects

    # Buscar tweets usando las palabras clave
    tweets = await search_tweets(Keywords)

    # Crear la respuesta
    response = ResponseModel(tweets=tweets)
    return response