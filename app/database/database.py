from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://parrot:security_parrot@localhost:5432/parrots"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


metadata = MetaData()

parrot_user_table = Table(
    "parrot_user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", Integer, nullable=False),
    Column("description", String),
)


def get_parrot_user(db: Session, user_id: int):
    return db.query(parrot_user_table).filter(parrot_user_table.c.id == user_id).first()
