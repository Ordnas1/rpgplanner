from datetime import datetime
from sqlalchemy import inspect

from src import db


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

    def to_dict(self):
        """Serialize to json"""
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        return f"{self.name}"
