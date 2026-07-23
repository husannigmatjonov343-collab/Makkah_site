from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session, joinedload

from app.database import get_db
from app import models

router = APIRouter(tags=["Pages"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    steps = db.query(models.UmrahStep).order_by(models.UmrahStep.step_number).all()
    categories = db.query(models.Category).order_by(models.Category.order_index).all()
    duas_count = db.query(models.Dua).count()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "steps": steps[:3], "categories": categories, "duas_count": duas_count, "active": "home"},
    )


@router.get("/tarix")
def tarix_page(request: Request, db: Session = Depends(get_db)):
    category = (
        db.query(models.Category)
        .options(joinedload(models.Category.articles))
        .filter(models.Category.slug == "tarix")
        .first()
    )
    return templates.TemplateResponse("category.html", {"request": request, "category": category, "active": "tarix"})


@router.get("/fazilatlar")
def fazilatlar_page(request: Request, db: Session = Depends(get_db)):
    category = (
        db.query(models.Category)
        .options(joinedload(models.Category.articles))
        .filter(models.Category.slug == "fazilatlar")
        .first()
    )
    return templates.TemplateResponse("category.html", {"request": request, "category": category, "active": "fazilatlar"})


@router.get("/maqola/{slug}")
def article_detail(slug: str, request: Request, db: Session = Depends(get_db)):
    article = db.query(models.Article).filter(models.Article.slug == slug).first()
    if not article:
        raise HTTPException(status_code=404, detail="Maqola topilmadi")
    related = (
        db.query(models.Article)
        .filter(models.Article.category_id == article.category_id, models.Article.id != article.id)
        .order_by(models.Article.order_index)
        .limit(3)
        .all()
    )
    return templates.TemplateResponse(
        "article.html",
        {"request": request, "article": article, "related": related, "active": article.category.slug},
    )


@router.get("/umra")
def umra_page(request: Request, db: Session = Depends(get_db)):
    steps = db.query(models.UmrahStep).order_by(models.UmrahStep.step_number).all()
    return templates.TemplateResponse("umrah.html", {"request": request, "steps": steps, "active": "umra"})


@router.get("/duolar")
def duolar_page(request: Request, db: Session = Depends(get_db)):
    duas = db.query(models.Dua).order_by(models.Dua.order_index).all()
    return templates.TemplateResponse("duas.html", {"request": request, "duas": duas, "active": "duolar"})


@router.get("/savol-javob")
def faq_page(request: Request, db: Session = Depends(get_db)):
    faqs = db.query(models.FAQ).order_by(models.FAQ.order_index).all()
    return templates.TemplateResponse("faq.html", {"request": request, "faqs": faqs, "active": "faq"})
