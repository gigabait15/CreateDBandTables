from database import Base, int_pk, str_pk
from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column


class Hashes(Base):
    """Класс для создания таблицы hashes"""
    __tablename__ = 'hashes'

    hash_id: Mapped[str_pk]
    user_name: Mapped[str]
    chat_id: Mapped[str] #
    date: Mapped[str] #
    amount: Mapped[int] = mapped_column(BigInteger, nullable=False)


    extend_existing = True

    def __repr__(self):
        return f"{self.__tablename__}(id={self.hash_id})"


class TransUsers(Base):
    """Класс для создания таблицы trans_users"""
    __tablename__ = 'trans_users'

    trans_id: Mapped[int_pk]
    trans_type: Mapped[str]
    amount: Mapped[int]
    user_name: Mapped[str]
    moder_user_name: Mapped[str]
    photo_path: Mapped[str]
    trans_date: Mapped[str]

    extend_existing = True

    def __repr__(self):
        return f"{self.__tablename__}(id={self.trans_id})"