from sqlalchemy.types import ARRAY, String

from database import Base, bool_false, bool_true, int_pk
from sqlalchemy.orm import Mapped, mapped_column


class ModelsDrawList(Base):
    """Класс для создания таблицы models_draw_list"""
    __tablename__ = 'models_draw_list'

    model_id: Mapped[int_pk]
    post_id: Mapped[int] = mapped_column(nullable = True)
    age: Mapped[int] = mapped_column(nullable = True)
    documents: Mapped[str] = mapped_column(nullable = True)  #
    platform: Mapped[str] = mapped_column(nullable = True)  #
    account: Mapped[str] = mapped_column(nullable = True)
    phone: Mapped[str] = mapped_column(nullable = True)
    time: Mapped[str] = mapped_column(nullable = True)
    taboo: Mapped[str] = mapped_column(nullable = True)  #
    social: Mapped[str] = mapped_column(nullable = True)
    language: Mapped[str] = mapped_column(nullable = True)  #
    percent: Mapped[int] = mapped_column(nullable = True)
    price: Mapped[int] = mapped_column(nullable = True)
    owner: Mapped[str] = mapped_column(nullable = True)
    photos: Mapped[list[str]] = mapped_column(ARRAY(String), nullable = True)
    actual: Mapped[bool_true]
    owner_chat_id: Mapped[str] = mapped_column(nullable = True)  #
    additional: Mapped[str] = mapped_column(nullable = True)
    model_id_order: Mapped[bool_false]

    extend_existing = True

    def __repr__(self):
        return f"{self.__tablename__}(id={self.model_id})"


class ModelsPosts(Base):
    """Класс для создания таблицы models_posts"""
    __tablename__ = 'models_posts'

    model_id: Mapped[int_pk]
    post_id: Mapped[int] = mapped_column(nullable = True)
    age: Mapped[int] = mapped_column(nullable = True)
    documents: Mapped[str] = mapped_column(nullable = True) #
    platform: Mapped[str] = mapped_column(nullable = True) #
    account: Mapped[str] = mapped_column(nullable = True)
    phone: Mapped[str] = mapped_column(nullable = True)
    time: Mapped[str] = mapped_column(nullable = True)
    taboo: Mapped[str] = mapped_column(nullable = True) #
    social: Mapped[str] = mapped_column(nullable = True)
    language: Mapped[str] = mapped_column(nullable = True) #
    percent: Mapped[int] = mapped_column(nullable = True)
    price: Mapped[int] = mapped_column(nullable = True)
    owner: Mapped[str] = mapped_column(nullable = True)
    photos: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=True)
    actual: Mapped[bool_true]
    owner_chat_id: Mapped[str] = mapped_column(nullable = True)#
    additional: Mapped[str] = mapped_column(nullable = True)
    model_id_order: Mapped[bool_false]

    extend_existing = True

    def __repr__(self):
        return f"{self.__tablename__}(id={self.model_id})"