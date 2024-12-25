from database import Base, bool_false, bool_true, int_pk
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column


class ModelsDrawList(Base):
    """Класс для создания таблицы models_draw_list"""
    __tablename__ = 'models_draw_list'

    model_id: Mapped[int_pk]
    post_id: Mapped[int]
    age: Mapped[int]
    documents: Mapped[str]  #
    platform: Mapped[str]  #
    account: Mapped[str]
    phone: Mapped[str]
    time: Mapped[str]
    taboo: Mapped[str]  #
    social: Mapped[str]
    language: Mapped[str]  #
    percent: Mapped[int]
    price: Mapped[int]
    owner: Mapped[str]
    photos: Mapped[list[str]] = mapped_column(JSONB)
    actual: Mapped[bool_true]
    owner_chat_id: Mapped[str]  #
    additional: Mapped[str]
    model_id_order: Mapped[bool_false]

    extend_existing = True

    def __repr__(self):
        return f"{self.__tablename__}(id={self.model_id})"


class ModelsPosts(Base):
    """Класс для создания таблицы models_posts"""
    __tablename__ = 'models_posts'

    model_id: Mapped[int_pk]
    post_id: Mapped[int]
    age: Mapped[int]
    documents: Mapped[str] #
    platform: Mapped[str] #
    account: Mapped[str]
    phone: Mapped[str]
    time: Mapped[str]
    taboo: Mapped[str] #
    social: Mapped[str]
    language: Mapped[str] #
    percent: Mapped[int]
    price: Mapped[int]
    owner: Mapped[str]
    photos: Mapped[list[str]] = mapped_column(JSONB)
    actual: Mapped[bool_true]
    owner_chat_id: Mapped[str] #
    additional: Mapped[str]
    model_id_order: Mapped[bool_false]

    extend_existing = True

    def __repr__(self):
        return f"{self.__tablename__}(id={self.model_id})"