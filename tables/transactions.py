from database import Base, int_pk, str_pk
from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column


class Hashes(Base):
    """Класс для создания таблицы hashes"""
    __tablename__ = 'hashes'

    hash_id: Mapped[str_pk]
    user_name: Mapped[str] = mapped_column(nullable = True)
    chat_id: Mapped[str] = mapped_column(nullable = True) #
    date: Mapped[str] = mapped_column(nullable = True) #
    amount: Mapped[int] = mapped_column(BigInteger, default = 0)


    extend_existing = True

    def __repr__(self):
        return f"{self.__tablename__}(id={self.hash_id})"


class TransUsers(Base):
    """Класс для создания таблицы trans_users"""
    __tablename__ = 'trans_users'

    trans_id: Mapped[int_pk]
    trans_type: Mapped[str] = mapped_column(nullable = True)
    amount: Mapped[int] = mapped_column(nullable = True)
    user_name: Mapped[str] = mapped_column(nullable = True)
    moder_user_name: Mapped[str] = mapped_column(nullable = True)
    photo_path: Mapped[str] = mapped_column(nullable = True)
    trans_date: Mapped[str] = mapped_column(nullable = True)

    extend_existing = True

    def __repr__(self):
        return f"{self.__tablename__}(id={self.trans_id})"