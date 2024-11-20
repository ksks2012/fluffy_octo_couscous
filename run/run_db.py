from datetime import datetime, timezone
from internal.dao import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import uuid

from internal.dao.comment import Comment
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
    
    try:
        session = SessionLocal()
        new_comment = Comment(
            thread_id=str(uuid.uuid4()),
            user_id="user123",
            post_title="This is a discussion title",
            comment_text="Great player performance!",
            topic="Player Performance",
            sentiment="Positive",
            sentiment_score=0.95,
            language="en",
            created_at=datetime.now(timezone.utc),
            processed_at=datetime.now(timezone.utc),
            vector_embedding=None
        )
        session.add(new_comment)
        session.commit()
        session.close()
    except Exception as e:
        print(e)
        return
    
# Create the table
if __name__ == "__main__":
    config = read_ini("./alembic.ini")
    create_connection(config["alembic"]["sqlalchemy.url"])