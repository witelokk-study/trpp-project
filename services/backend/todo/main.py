from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from . import auth, tasks, categories
from .database import SessionLocal, engine, Base


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


app = FastAPI()
app.add_middleware( CORSMiddleware, allow_origins=["*"],  allow_credentials=True, allow_methods=["*"], allow_headers=["*"], )

app.include_router(auth.router)
app.include_router(tasks.router)
app.include_router(categories.router)

Base.metadata.create_all(bind=engine)
