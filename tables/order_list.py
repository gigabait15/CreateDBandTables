from database import Base, bool_false, int_pk, int_pk_default
from sqlalchemy.orm import Mapped, mapped_column


class Orders(Base):
    """Класс для создания таблицы orders"""
    __tablename__ = 'orders'

    order_id: Mapped[int_pk]
    seller_chat_id: Mapped[str] #
    buyer_chat_id: Mapped[str] #
    amount_model: Mapped[int_pk_default]
    buyer_amount: Mapped[int_pk_default]
    expiration: Mapped[int] = mapped_column(default=10)
    model_id: Mapped[int]
    model_user_name: Mapped[str]
    order_status: Mapped[bool_false]
    seller_ready: Mapped[bool_false]
    buyer_ready: Mapped[bool_false]
    order_finished: Mapped[bool_false]
    date_open: Mapped[str]
    date_close: Mapped[str]
    seller_user_name: Mapped[str]
    buyer_user_name: Mapped[str]
    seller_fake_name: Mapped[str]
    buyer_fake_name: Mapped[str]
    barrier: Mapped[bool_false]

    extend_existing = True

    def __repr__(self):
        return f"{self.__tablename__}(id={self.order_id})"


class OrdersDraw(Base):
    """Класс для создания таблицы orders_draw"""
    __tablename__ = 'orders_draw'

    order_draw_id: Mapped[int_pk]
    model_id: Mapped[int]
    seller_user_name: Mapped[str]
    buyer_user_name: Mapped[str]
    seller_ready: Mapped[bool_false]
    buyer_ready: Mapped[bool_false]
    seller_chat_id: Mapped[str]
    buyer_chat_id: Mapped[str]
    seller_fake_name: Mapped[str]
    buyer_fake_name: Mapped[str]

    extend_existing = True

    def __repr__(self):
        return f"{self.__tablename__}(id={self.order_draw_id})"