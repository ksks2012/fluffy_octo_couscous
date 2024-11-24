from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, Session

from internal.dao import Base
from internal.dao.analysis_result import AnalysisResult
from internal.dao.comment import Comment
from internal.dao.search_log import SearchLog
from internal.dao.topic import Topic
from utils.file_processor import read_ini

class DBRoutine:
    def __init__(self, DATABASE_URL: str):
        self.DATABASE_URL = DATABASE_URL
        self.create_db_if_not_exists()
        self.create_connection()

    def create_db_if_not_exists(self) -> None:
        self.engine = create_engine(self.DATABASE_URL, connect_args={"check_same_thread": False})
        try:
            Base.metadata.create_all(bind=self.engine)
            print("SQLite database table created.")
        except Exception as e:
            print(e)
            return

    def create_connection(self) -> None:
        # Database engine and session
        self.session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

        try:
            self.connection = self.engine.connect()
            print("SQLite database connected.")
        except Exception as e:
            print(e)
            return
    
    # TODO: Save list of comments
    def save_comment(self, comment: Comment) -> bool:
        """
        Saves a Comment object to the database.
        :param comment: Comment instance
        :return: True if successful, False otherwise
        """
        session: Session = self.session_local()
        try:
            # Validate that the analysis_id exists in the AnalysisResult table (if provided)
            if comment.analysis_id:
                analysis_result = session.query(AnalysisResult).filter_by(analysis_id=comment.analysis_id).first()
                if not analysis_result:
                    print(f"Error: Analysis ID {comment.analysis_id} does not exist.")
                    return False

            session.add(comment)
            session.commit()
            print(f"Saved Comment with ID: {comment.id}")
            return True
        except SQLAlchemyError as e:
            print(f"Error saving Comment: {e}")
            session.rollback()
            return False
        finally:
            session.close()
        
    # TODO: Save list of analysis results
    def save_analysis_result(self, result: AnalysisResult) -> bool:
        """
        Saves an AnalysisResult object to the database.
        :param result: AnalysisResult instance
        :return: True if successful, False otherwise
        """
        result.hash_value = result.generate_hash()
        session: Session = self.session_local()
        try:
            session.add(result)
            session.commit()
            print(f"Saved AnalysisResult with ID: {result.analysis_id}")
            return True
        except SQLAlchemyError as e:
            print(f"Error saving AnalysisResult: {e}")
            session.rollback()
            return False
        finally:
            session.close()

# Create the table
if __name__ == "__main__":
    config = read_ini("./alembic.ini")
    db_routine = DBRoutine(config["alembic"]["sqlalchemy.url"])