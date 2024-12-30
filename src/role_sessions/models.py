from typing import List
from datetime import datetime
from sqlalchemy import inspect, Integer, String, DateTime, Table, Column, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src import db, Base
from src.auth.models import User

session_player_table = Table(
    "session_players_table",
    Base.metadata,
    Column("session_id", ForeignKey("role_session.id")),
    Column("player_id", ForeignKey("player.id")),
)


class RoleSession(db.Model):  # type: ignore[name-defined]
    """RoleSession Model"""

    id = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    created_on = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated_on = db.Column(
        db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now
    )

    name = db.Column(db.String(50), nullable=False)
    start_time = db.Column(db.DateTime(timezone=True), nullable=False)
    end_time = db.Column(db.DateTime(timezone=True), nullable=False)
    role_system_id: Mapped[int] = mapped_column(ForeignKey('role_system.id'))
    role_system: Mapped["RoleSystem"] = relationship()
    players: Mapped[List["Player"]] = relationship(secondary=session_player_table)

    def to_dict(self):
        """Serialize to json"""
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        return f"{self.name}"


class RoleSystem(db.Model):
    """A Game system for a roleplaying game"""

    id: Mapped[int] = mapped_column(Integer, unique=True, primary_key=True)
    created_on: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), default=datetime.now
    )
    updated_on: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), default=datetime.now, onupdate=datetime.now
    )

    name: Mapped[str] = mapped_column(String(80), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    creator_id: Mapped[str] = mapped_column(ForeignKey('user.id'))
    creator: Mapped["User"] = relationship()


class Player(db.Model):
    id: Mapped[int] = mapped_column(Integer, unique=True, primary_key=True)
    created_on: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), default=datetime.now
    )
    updated_on: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), default=datetime.now, onupdate=datetime.now
    )
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
