from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from app.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(64), unique=True, index=True, nullable=False)
    title = Column(String(200), nullable=False)
    subtitle = Column(String(300), nullable=True)
    description = Column(Text, nullable=True)
    icon = Column(String(64), nullable=True)  # emoji yoki ikon nomi
    order_index = Column(Integer, default=0)

    articles = relationship("Article", back_populates="category", order_by="Article.order_index")


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    slug = Column(String(150), unique=True, index=True, nullable=False)
    title = Column(String(250), nullable=False)
    summary = Column(String(400), nullable=True)
    quick_fact = Column(String(200), nullable=True)  # yon panelda ko'rsatiladigan qisqa fakt
    body = Column(Text, nullable=False)
    order_index = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    category = relationship("Category", back_populates="articles")


class UmrahStep(Base):
    __tablename__ = "umrah_steps"

    id = Column(Integer, primary_key=True, index=True)
    step_number = Column(Integer, nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    arabic_text = Column(String(500), nullable=True)
    transliteration = Column(String(500), nullable=True)
    meaning = Column(String(500), nullable=True)
    tip = Column(String(400), nullable=True)


class Dua(Base):
    __tablename__ = "duas"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(150), unique=True, index=True, nullable=False)
    title = Column(String(200), nullable=False)
    tag = Column(String(60), nullable=True)  # filtrlash uchun: Ihrom, Tavof, Sa'y, Zamzam...
    occasion = Column(String(200), nullable=True)  # qachon o'qiladi
    arabic_text = Column(Text, nullable=True)
    transliteration = Column(Text, nullable=True)
    translation = Column(Text, nullable=True)
    order_index = Column(Integer, default=0)


class FAQ(Base):
    __tablename__ = "faqs"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String(300), nullable=False)
    answer = Column(Text, nullable=False)
    tag = Column(String(60), nullable=True)  # Umumiy, Ihrom, Moliya, Sog'liq...
    order_index = Column(Integer, default=0)
