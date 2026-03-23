from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ArticleBase(BaseModel):
    # min_length=1 empêche d'envoyer un texte vide ""
    title: str = Field(..., min_length=1, description="Le titre de l'article")
    content: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    category: str
    tags: str

class ArticleCreate(ArticleBase):
    pass

class ArticleResponse(ArticleBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
