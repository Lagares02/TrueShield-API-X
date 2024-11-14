from fastapi import APIRouter, HTTPException
from models.models import RequestModel
from services.x import search_tweets

router = APIRouter()

@router.get("/")
async def home():
    return {"message": "Bienvenido!"}


@router.post("/contrasting_x")
async def contrasting(request: RequestModel):
    try:
        print("Recibido!!!")
        keywords = request.keywords.keywords_en + request.subjects
        
        prompt = request.prompt
        
        results = search_tweets(keywords)
        
        return {
            "X": results
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))