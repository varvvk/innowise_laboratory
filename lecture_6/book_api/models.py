from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Optional
from sqlalchemy import event
from sqlalchemy.engine import Connection


class Base(DeclarativeBase):
    pass

class BookOrm(Base):
    __tablename__: str = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    year: Mapped[Optional[int]] = mapped_column(nullable=True)

@event.listens_for(BookOrm, "before_update")
def validate_book(
    mapper,
    connection: Connection,
    target: BookOrm) -> None:
    if not target.title.strip() or not target.author.strip():
        raise ValueError("Title and Author cannot be empty")
