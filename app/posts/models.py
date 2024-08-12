from datetime import datetime

from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database import Base


class Posts(Base):
    __tablename__ = 'Posts'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
        nullable=False
    )
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    author_id: Mapped[int] = mapped_column(
        ForeignKey('User.id'),
        nullable=False
    )
    company_id: Mapped[int] = mapped_column(
        ForeignKey('Companies.id'),
        nullable=False
    )
    category_id: Mapped[int] = mapped_column(ForeignKey('Categories.id'), nullable=False)
    pub_date: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(),
        nullable=False
    )
    pub_updated: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(),
        onupdate=datetime.now(),
        nullable=False
    )


class Categories(Base):
    __tablename__ = 'Categories'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
        nullable=False
    )
    name: Mapped[str] = mapped_column(nullable=False)


class Companies(Base):
    __tablename__ = 'Companies'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
        nullable=False
    )
    name: Mapped[str] = mapped_column(nullable=False)
