from flask_bcrypt import Bcrypt
from sqlalchemy import func

from app import db
from app.models import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    bcrypt: Bcrypt = Bcrypt()

    username = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )
    password_hash = db.Column(
        db.String(255),
        nullable=False
    )
    created_at = db.Column(
        db.DateTime,
        default=func.now(),
        nullable=False
    )

    def __str__(self):
        return f"{self.id}. {self.username}"

    def set_password(
            self,
            password: str
    ) -> None:
        """
        Hash and set the password
        """
        self.password_hash = self.bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(
            self,
            password: str
    ) -> bool:
        """
        Check if the password matches the hash
        """
        return self.bcrypt.check_password_hash(self.password_hash, password)
