from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/api/v1", tags=["API"])


@router.get("/categories", response_model=list[schemas.CategoryOut])
def list_categories(db: Session = Depends(get_db)):
    return (
        db.query(models.Category)
        .options(joinedload(models.Category.articles))
        .order_by(models.Category.order_index)
        .all()
    )


@router.get("/categories/{slug}", response_model=schemas.CategoryOut)
def get_category(slug: str, db: Session = Depends(get_db)):
    category = (
        db.query(models.Category)
        .options(joinedload(models.Category.articles))
        .filter(models.Category.slug == slug)
        .first()
    )
    if not category:
        raise HTTPException(status_code=404, detail="Kategoriya topilmadi")
    return category


@router.get("/articles/{slug}", response_model=schemas.ArticleOut)
def get_article(slug: str, db: Session = Depends(get_db)):
    article = db.query(models.Article).filter(models.Article.slug == slug).first()
    if not article:
        raise HTTPException(status_code=404, detail="Maqola topilmadi")
    return article


@router.get("/umrah-steps", response_model=list[schemas.UmrahStepOut])
def list_umrah_steps(db: Session = Depends(get_db)):
    return db.query(models.UmrahStep).order_by(models.UmrahStep.step_number).all()


@router.get("/duas", response_model=list[schemas.DuaOut])
def list_duas(db: Session = Depends(get_db)):
    return db.query(models.Dua).order_by(models.Dua.order_index).all()


@router.get("/duas/{slug}", response_model=schemas.DuaOut)
def get_dua(slug: str, db: Session = Depends(get_db)):
    dua = db.query(models.Dua).filter(models.Dua.slug == slug).first()
    if not dua:
        raise HTTPException(status_code=404, detail="Duo topilmadi")
    return dua


@router.get("/faqs", response_model=list[schemas.FAQOut])
def list_faqs(db: Session = Depends(get_db)):
    return db.query(models.FAQ).order_by(models.FAQ.order_index).all()
