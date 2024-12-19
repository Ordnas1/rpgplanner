from datetime import datetime

from sqlalchemy import String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from src import db


class User(db.Model):
    id: Mapped[str] = mapped_column(String(50), primary_key=True, unique=True)
    created_on: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=datetime.now)

    username: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(80), nullable=False)
    email: Mapped[str] = mapped_column(String(80), nullable=False, unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    nickname: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)

