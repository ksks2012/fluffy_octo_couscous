from datetime import datetime, timezone
from internal.dao import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import uuid

from internal.dao.comment import Comment
from internal.dao.search_log import SearchLog
from internal.dao.topic import Topic
from utils.file_processor import read_ini

def create_connection(DATABASE_URL: str) -> None:
    # Database engine and session
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    try:
        Base.metadata.create_all(bind=engine)
        print("SQLite database table created.")
    except Exception as e:
        print(e)
        return
    
    try:
        connection = engine.connect()
        print("SQLite database connected.")
    except Exception as e:
        print(e)
        return

# Create the table
if __name__ == "__main__":
    config = read_ini("./alembic.ini")
    create_connection(config["alembic"]["sqlalchemy.url"])
