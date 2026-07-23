from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import settings
from app.database import Base, engine
from app.routers import pages, api

# Jadvallarni avtomatik yaratish (ishlab chiqarishda Alembic migratsiyasidan foydalaning)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    description="Makkai Mukarrama va Umra haqida ma'lumotlar bazasi asosidagi sayt",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(pages.router)
app.include_router(api.router)
