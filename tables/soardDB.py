from database import Base, bool_false, int_default, int_pk_default, str_pk
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import ARRAY, String


class BannedUsers(Base):
    """Класс для создания таблицы banned_users"""
    __tablename__ = 'banned_users'

    user_name: Mapped[str_pk]
    chat_id: Mapped[str] #
    reason: Mapped[str]

    extend_existing = True

    def __repr__(self):
        return f"{self.__tablename__}(id={self.user_name})"


class CommonData(Base):
    """Класс для создания таблицы common_data"""
    __tablename__ = 'common_data'

    key: Mapped[int_pk_default]
    percent: Mapped[int_default]
    monthone: Mapped[int_default]
    monththree: Mapped[int_default]
    monthsix: Mapped[int_default]
    monthwelve: Mapped[int_default]
    subs_status: Mapped[bool_false]
    admins: Mapped[list[str]] = mapped_column(ARRAY(String))


    extend_existing = True

    def __repr__(self):
        return f"{self.__tablename__}(id={self.key})"


class Users(Base):
    """Класс для создания таблицы users"""
    __tablename__ = 'users'

    user_name: Mapped[str_pk]
    balance: Mapped[int_default]
    model_id: Mapped[list[int]] = mapped_column(ARRAY(String))
    user_id: Mapped[str] #
    chat_id: Mapped[str] #
    terms_one: Mapped[bool_false]
    terms_two: Mapped[bool_false]
    user_wallet: Mapped[str]
    user_type: Mapped[str]
    model_id_draw: Mapped[list[int]] = mapped_column(ARRAY(String))
    order_id_list: Mapped[list[int]] = mapped_column(ARRAY(String))
    banned: Mapped[bool_false]
    subscription: Mapped[bool_false]
    subscription_ex: Mapped[int_default]
    fake_name: Mapped[str]
    chat_room_ids: Mapped[list[int]] = mapped_column(ARRAY(String))
    opened_count: Mapped[int]
    finished_count: Mapped[int]

    extend_existing = True

    def __repr__(self):
        return f"{self.__tablename__}(id={self.user_name})"
