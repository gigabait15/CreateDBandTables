import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine, text

load_dotenv()

DB_NAME = ['dialogue_list', 'model', 'order_list', 'soardDB', 'stock', 'transactions']


def create_database():
    """
    Функция создания баз данных из списка
    Создается подключения к БД, далее при успешном подключении в цикле подставляются именя БД для создания
    :return: консольные логи процесса создания БД
    """
    temp_engine = create_engine(
        f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}"
        f"@{settings.DB_HOST}:{settings.DB_PORT}",
        isolation_level='AUTOCOMMIT'
    )

    with temp_engine.connect() as conn:
        try:
            for name_db in DB_NAME:
                conn.execute(text(f'CREATE DATABASE "{name_db}";'))
                print(f'База данных {name_db} успешно создана')
        except Exception as e:
            print(f'Ошибка при создании БД {name_db}: {e}')
        finally:
            conn.close()

def get_db_async_url(db_name: str) -> str:
    """
    Функция возвращает ссылку для асинхронного подключение к БД
    :param db_name: имя БД к которой нужно получить ссылку для подключения
    :return: ссылку для асинхронного подключения
    """

    return (f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}"
            f"@{settings.DB_HOST}:{settings.DB_PORT}/{db_name}")

def get_db_url(db_name: str) -> str:
    """
    Функция возвращает ссылку для подключение к БД
    :param db_name: имя БД к которой нужно получить ссылку для подключения
    :return: ссылку для подключения
    """

    return (f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}"
            f"@{settings.DB_HOST}:{settings.DB_PORT}/{db_name}")

class Settings(BaseSettings):
    """
    Класс модели для доступа к переменным окружения
    Переменные подтягиваются с файла с переменными окружения для дальнейшего использования
    """
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str

    # Для обнаруженния переменных окружения
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    )


# объявление переменной для обрашение к экземпляру класса
settings = Settings()
