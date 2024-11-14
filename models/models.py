from pydantic import BaseModel
from typing import List

class KeywordsModel(BaseModel):
    keywords_en: list[str]
    keywords_es: list[str]

class RequestModel(BaseModel):
    prompt: str
    temporality: str
    location: List[str]
    keywords: KeywordsModel
    subjects: List[str]

class TweetModel(BaseModel):
    Id: str
    DatePub: str
    UserProfile: str
    NameProfile: str
    TextPub: str
    CantLike: int
    CantRetwits: int
    CantComents: int
    Confidence: float = 0.60  # Valor predeterminado
    matches: int
    Domain: float
    Inference: float
    Type_item: str