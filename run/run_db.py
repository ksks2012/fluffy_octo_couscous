from datetime import datetime, timezone
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
import uuid

from internal.dao.analysis_result import AnalysisResult
from internal.dao.comment import Comment
from internal.dao.dbroutine import DBRoutine
from utils.file_processor import read_ini

class DBHandler:
    def __init__(self, config_path: str):
        self.config = read_ini(config_path)
        self.db_routine = DBRoutine(self.config["alembic"]["sqlalchemy.url"])

    def run_all(self) -> None:
        self.run_save_analysis_result()
        self.run_save_comment()

    def run_save_comment(self) -> None:
        # Create or fetch an existing AnalysisResult object
        session: Session = self.db_routine.session_local()
        try:
            # Assuming we want to reference an existing analysis
            analysis_result = session.query(AnalysisResult).first()
            if not analysis_result:
                # If no analysis exists, create one for testing
                analysis_result = AnalysisResult(
                    sentiment="Positive",
                    sentiment_score=0.9,
                    topic="Game Outcome",
                    model_name="TestModel",
                    temperature=0.7,
                    top_k=40,
                    top_p=0.95,
                    mode="test",
                    prompt="Analyze this comment."
                )
                session.add(analysis_result)
                session.commit()
                print(f"Created AnalysisResult with ID: {analysis_result.analysis_id}")

            # Create a new comment referencing this analysis_id
            new_comment = Comment(
                thread_id=str(uuid.uuid4()),
                user_id="user123",
                post_title="This is a discussion title",
                comment_text="Great player performance!",
                language="en",
                created_at=datetime.now(timezone.utc),
                processed_at=datetime.now(timezone.utc),
                vector_embedding=None,
                analysis_id=analysis_result.analysis_id  # Link to the analysis result
            )

            # Save the comment using save_comment
            success = self.db_routine.save_comment(new_comment)
            if success:
                print("Comment saved successfully.")
            else:
                print("Failed to save comment.")
        except SQLAlchemyError as e:
            print(f"Error during run_save_comment: {e}")
            session.rollback()
        finally:
            session.close()

    def run_save_analysis_result(self) -> None:
        new_analysis_result = AnalysisResult(
            sentiment="Positive",
            sentiment_score=0.95,
            topic="Test Topic",
            model_name="Test Model",
            temperature=0.7,
            top_k=50,
            top_p=0.9,
            mode="test",
            prompt="This is a test prompt."
        )

        # Save to the database
        success = self.db_routine.save_analysis_result(new_analysis_result)
        if success:
            print("Analysis result saved successfully.")
        else:
            print("Failed to save analysis result.")

# Create the table
if __name__ == "__main__":
    db_handler = DBHandler("./alembic.ini")
    db_handler.run_all()