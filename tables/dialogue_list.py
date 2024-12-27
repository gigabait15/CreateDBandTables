from database import Base, dt, int_pk
from sqlalchemy.orm import Mapped, mapped_column


class Dialogue(Base):
    """Класс для создания таблицы dialogue"""
    __tablename__ = 'dialogue'

    dialogue_id: Mapped[int_pk]
    model_id: Mapped[int] = mapped_column(nullable = True)
    seller_chat_id: Mapped[str] = mapped_column(nullable = True) #
    seller_user_name: Mapped[str] = mapped_column(nullable = True)
    buyer_chat_id: Mapped[str] = mapped_column(nullable = True) #
    buyer_user_name: Mapped[str] = mapped_column(nullable = True)
    chat_id: Mapped[str] = mapped_column(nullable = True)
    date: Mapped[dt] = mapped_column(nullable = True)
    message: Mapped[str] = mapped_column(nullable = True)

    extend_existing = True

    def __repr__(self):
        return f"{self.__tablename__}(id={self.dialogue_id})"


class Pass(Base):
    """Класс для создания таблицы pass"""
    __tablename__ = 'pass'

    id: Mapped[int_pk]
    mail: Mapped[str] = mapped_column(nullable = True)
    password: Mapped[str] = mapped_column(nullable = True)

    extend_existing = True

    def __repr__(self):
        return f"{self.__tablename__}(id={self.id})"