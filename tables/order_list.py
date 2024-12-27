from database import Base, bool_false, int_pk, int_pk_default
from sqlalchemy.orm import Mapped, mapped_column


class Orders(Base):
    """Класс для создания таблицы orders"""
    __tablename__ = 'orders'

    order_id: Mapped[int_pk]
    seller_chat_id: Mapped[str] = mapped_column(nullable = True) #
    buyer_chat_id: Mapped[str] = mapped_column(nullable = True) #
    amount_model: Mapped[int_pk_default]
    buyer_amount: Mapped[int_pk_default]
    expiration: Mapped[int] = mapped_column(default=10)
    model_id: Mapped[int] = mapped_column(nullable = True)
    model_user_name: Mapped[str] = mapped_column(nullable = True)
    order_status: Mapped[bool_false]
    seller_ready: Mapped[bool_false]
    buyer_ready: Mapped[bool_false]
    order_finished: Mapped[bool_false]
    date_open: Mapped[str] = mapped_column(nullable = True)
    date_close: Mapped[str] = mapped_column(nullable = True)
    seller_user_name: Mapped[str] = mapped_column(nullable = True)
    buyer_user_name: Mapped[str] = mapped_column(nullable = True)
    seller_fake_name: Mapped[str] = mapped_column(nullable = True)
    buyer_fake_name: Mapped[str] = mapped_column(nullable = True)
    barrier: Mapped[bool_false]

    extend_existing = True

    def __repr__(self):
        return f"{self.__tablename__}(id={self.order_id})"


class OrdersDraw(Base):
    """Класс для создания таблицы orders_draw"""
    __tablename__ = 'orders_draw'

    order_draw_id: Mapped[int_pk]
    model_id: Mapped[int] = mapped_column(nullable = True)
    seller_user_name: Mapped[str] = mapped_column(nullable = True)
    buyer_user_name: Mapped[str] = mapped_column(nullable = True)
    seller_ready: Mapped[bool_false]
    buyer_ready: Mapped[bool_false]
    seller_chat_id: Mapped[str] = mapped_column(nullable = True)
    buyer_chat_id: Mapped[str] = mapped_column(nullable = True)
    seller_fake_name: Mapped[str] = mapped_column(nullable = True)
    buyer_fake_name: Mapped[str] = mapped_column(nullable = True)

    extend_existing = True

    def __repr__(self):
        return f"{self.__tablename__}(id={self.order_draw_id})"