from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session

from .models import Base


engine: Engine = create_engine(
    "sqlite:///books.db",
    connect_args={"check_same_thread": False},
    echo=True)

SessionLocal: sessionmaker[Session] = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False)


def create_db() -> None:
    Base.metadata.create_all(bind=engine)
