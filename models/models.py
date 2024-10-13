from pydantic import BaseModel
from typing import List

class RequestModel(BaseModel):
    prompt: str
    temporality: str
    location: str
    keywords: List[str]
    main_topic: str
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
    TrueLevel: float = 0.60  # Valor predeterminado
    matches: int
    ContextLevel: float
    Type_item: str

class ResponseModel(BaseModel):
    tweets: List[TweetModel]
