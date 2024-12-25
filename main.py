from config import create_database
from database import create_tables
import time


if __name__ == "__main__":
    create_database()
    time.sleep(1)
    create_tables()




