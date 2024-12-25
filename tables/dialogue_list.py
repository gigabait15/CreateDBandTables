from database import Base, dt, int_pk
from sqlalchemy.orm import Mapped


class Dialogue(Base):
    """Класс для создания таблицы dialogue"""
    __tablename__ = 'dialogue'

    dialogue_id: Mapped[int_pk]
    model_id: Mapped[int]
    seller_chat_id: Mapped[str] #
    seller_user_name: Mapped[str]
    buyer_chat_id: Mapped[str] #
    buyer_user_name: Mapped[str]
    chat_id: Mapped[str]
    date: Mapped[dt]
    message: Mapped[str]

    extend_existing = True

    def __repr__(self):
        return f"{self.__tablename__}(id={self.dialogue_id})"


class Pass(Base):
    """Класс для создания таблицы pass"""
    __tablename__ = 'pass'

    id: Mapped[int_pk]
    mail: Mapped[str]
    password: Mapped[str]

    extend_existing = True

    def __repr__(self):
        return f"{self.__tablename__}(id={self.id})"