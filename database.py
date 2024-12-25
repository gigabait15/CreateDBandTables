from datetime import datetime
from typing import Annotated

from sqlalchemy.ext.asyncio import (AsyncAttrs, AsyncSession,
                                    create_async_engine)
from sqlalchemy.orm import (DeclarativeBase, declared_attr, mapped_column,
                            sessionmaker)

from config import DB_NAME, get_db_async_url, get_db_url

from sqlalchemy import text, create_engine
import importlib


def all_session():
    """
    Функция для создания ссылок для подключения к БД, сессий для БД и фабрик асинхронных сессий
    сохраняет даннные в словарь, для быстрого доступа
    :return: словарь с данными для каждой БД
    """
    db_connections = {}

    for db_name in DB_NAME:
        # для асинхронки
        db_async_url = get_db_async_url(db_name)
        async_engine = create_async_engine(db_async_url, echo=True)
        async_session_maker = sessionmaker(
            async_engine,
            class_=AsyncSession,
            expire_on_commit=False
        )
        # Для классики
        db_url = get_db_url(db_name)
        engine = create_engine(db_url, echo=True)

        db_connections[db_name] = {
            'db_async_url': db_async_url,
            'async_engine': async_engine,
            'async_session_maker': async_session_maker,
            'db_url': db_url,
            'engine': engine
        }
    return db_connections

def table_exists(conn, table_name):
    """
    Функция для проверки наличия таблицы в базе данных.
    :param conn: подключение к БД
    :param table_name: Имя таблицы для проверки
    :return: True если таблица существует, иначе False
    """
    result = conn.execute(
        text(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = :table_name);"),
        {'table_name': table_name}
    )
    return result.scalar()  # Возвращает True или False


def create_tables():
    """
    Синхронная функция для создания таблиц во всех БД.
    Принцип работы: получаем имена БД и сессии из функции all_session, создаем метаданные для таблиц каждой БД.
    Создается подключение для каждой БД with engine.connect(), вывод в консоль текущей БД, проверка наличия таблиц.
    metadata.clear() очистка метаданных, чтобы не дублировать таблицы в другие БД
    """
    for session_name, session_data in all_session().items():
        module = importlib.import_module(f"tables.{session_name}")
        metadata = module.Base.metadata
        engine = session_data['engine']

        with engine.connect() as conn:
            current_db = conn.execute(text("SELECT current_database();")).scalar()
            print(f"Подключение к базе данных: {current_db}")

            try:
                for table in metadata.tables.values():
                    if table_exists(conn, table.name):
                        print(f"Таблица {table.name} уже существует в базе {current_db}.")
                    else:
                        try:
                            table.create(conn)
                            print(f"Таблица {table.name} успешно создана в базе {current_db}.")
                            conn.commit()
                        except Exception as e:
                            print(f'Ошибка при создании таблицы {table.name} в базе {current_db}: {e}')
            except Exception as e:
                print(f"Ошибка при выполнении транзакции для базы {current_db}: {e}")
        metadata.clear()


    # настройка аннотаций
int_pk = Annotated[int, mapped_column(primary_key=True)]
int_default = Annotated[int, mapped_column(default=0)]
int_pk_default = Annotated[int, mapped_column(primary_key=True, default=1)]

str_pk = Annotated[str, mapped_column(primary_key=True)]

dt = Annotated[datetime, mapped_column(nullable=False)]

bool_false = Annotated[bool, mapped_column(default=False)]
bool_true = Annotated[bool, mapped_column(default=True)]


class Base(AsyncAttrs, DeclarativeBase):
    """
    Абстрактный класс для создания таблиц
    __tablename__ используется для автоматического создания имени для таблицы
    """
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__tablename__}"
