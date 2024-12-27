from database import Base, bool_false, bool_true, int_pk, int_pk_default
from sqlalchemy.orm import Mapped, mapped_column


class ChatStock(Base):
    """Класс для создания таблицы chat_stock"""
    __tablename__ = 'chat_stock'

    chat_id: Mapped[int_pk_default]
    chat_buyer: Mapped[str] = mapped_column(nullable = True)
    chat_seller: Mapped[str] = mapped_column(nullable = True)
    seller_chat_id: Mapped[str] = mapped_column(nullable = True) #
    buyer_chat_id: Mapped[str] = mapped_column(nullable = True) #
    seller_user_name: Mapped[str] = mapped_column(nullable = True)
    buyer_user_name: Mapped[str] = mapped_column(nullable = True)
    seller_fake_name: Mapped[str] = mapped_column(nullable = True)
    buyer_fake_name: Mapped[str] = mapped_column(nullable = True)
    open: Mapped[bool_true]
    model_id: Mapped[int] = mapped_column(nullable = True)
    order_created: Mapped[bool_false]
    seller_joined: Mapped[bool_false]
    buyer_joined: Mapped[bool_false]
    order_id: Mapped[int] = mapped_column(nullable = True)

    extend_existing = True

    def __repr__(self):
        return f"{self.__tablename__}(id={self.chat_id})"


class Queue(Base):
    """Класс для создания таблицы queue"""
    __tablename__ = 'queue'

    queue_id: Mapped[int_pk]
    model_id: Mapped[int] = mapped_column(nullable = True)
    buyer_chat_id: Mapped[str] = mapped_column(nullable = True) #
    seller_id: Mapped[int] = mapped_column(nullable = True)

    extend_existing = True

    def __repr__(self):
        return f"{self.__tablename__}(id={self.queue_id})"