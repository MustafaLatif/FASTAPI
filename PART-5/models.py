from __future__ import annotations
from datetime import UTC , datetime
from sqlalchemy import ForeignKey, String, Integer, text, DateTime
from sqlalchemy.orm import Mapped , mapped_column,relationship
from database import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(120),
        unique=True,
        nullable=False
    )

    posts: Mapped[list[Post]] = relationship(
        back_populates="author"
    )

    class Post(Base):
        __tablename__ = "posts"

        id:Mapped[int] = mapped_column(
            Integer,
            primary_key=True,
            index=True
        )

        title: Mapped[int] = mapped_column(
            String(100),
            nullable= False

        )

        content:Mapped[str] = mapped_column(
            text,
            nullable=False
        )

        created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            default=lambda: datetime.now(UTC)
        )

        user_id: Mapped[int] = mapped_column(
            ForeignKey("users.id"),
            nullable=False
        )

        author: Mapped[User] = relationship(
            back_populates="posts"
        )