from datetime import datetime, timezone
from internal.dao import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import uuid

from internal.dao.comment import Comment
from internal.dao.dbroutine import DBRoutine
from utils.file_processor import read_ini

def run_db_routine() -> None:
    config = read_ini("./alembic.ini")
    db_routine = DBRoutine(config["alembic"]["sqlalchemy.url"])
    
    try:
        session = db_routine.session_local()
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
    run_db_routine()