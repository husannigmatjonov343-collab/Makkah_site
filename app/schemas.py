from datetime import datetime
from pydantic import BaseModel, ConfigDict


class ArticleOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    slug: str
    title: str
    summary: str | None = None
    quick_fact: str | None = None
    body: str
    order_index: int
    created_at: datetime | None = None


class ArticleBrief(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    slug: str
    title: str
    summary: str | None = None
    quick_fact: str | None = None


class CategoryOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    slug: str
    title: str
    subtitle: str | None = None
    description: str | None = None
    icon: str | None = None
    articles: list[ArticleBrief] = []


class UmrahStepOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    step_number: int
    title: str
    description: str
    arabic_text: str | None = None
    transliteration: str | None = None
    meaning: str | None = None
    tip: str | None = None


class DuaOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    slug: str
    title: str
    tag: str | None = None
    occasion: str | None = None
    arabic_text: str | None = None
    transliteration: str | None = None
    translation: str | None = None


class FAQOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    question: str
    answer: str
    tag: str | None = None
