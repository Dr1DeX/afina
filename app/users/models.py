from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database import Base


class User(Base):
    __tablename__ = 'User'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
        nullable=False
    )
    name: Mapped[Optional[str]] = mapped_column(nullable=False)
    username: Mapped[Optional[str]] = mapped_column(nullable=False)
    email: Mapped[Optional[str]] = mapped_column(nullable=False)
    google_access_token: Mapped[Optional[str]] = mapped_column(nullable=True)
    yandex_access_token: Mapped[Optional[str]] = mapped_column(nullable=True)
