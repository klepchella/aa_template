from database import database
from fastapi import APIRouter, Depends
from pydantic import PositiveInt
from repository.types import ParrotUser
from sqlalchemy.orm import Session

database.Base.metadata.create_all(bind=database.engine)

api_router = APIRouter()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@api_router.get("/user/{user_id}", response_model=ParrotUser)
async def get_genres(user_id: PositiveInt, db: Session = Depends(get_db)) -> ParrotUser:
    parrot_user = database.get_parrot_user(db, user_id)
    return parrot_user
