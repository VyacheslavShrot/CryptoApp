from app import db


class ModelMeta(type(db.Model)):
    """
    Meta CLass for Models
    """

    def __new__(
            cls,
            name,
            bases,
            dct
    ):
        if name != "BaseModel":
            # Check if __tablename__ attr Exist
            if "__tablename__" not in dct:
                raise AttributeError(f"Model '{name}' Must Define a '__tablename__' Attribute ")

        return super().__new__(cls, name, bases, dct)


class BaseModel(db.Model, metaclass=ModelMeta):
    """
    Base Structure of Every Model
    """

    __abstract__ = True

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
