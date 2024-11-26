from sqlalchemy import (
    Column,
    String,
    Text,
    ForeignKey,
    TIMESTAMP,
)

import uuid
import datetime

from internal.dao import Base

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
    thread_id = Column(String(36), nullable=False)
    user_id = Column(String(50), nullable=False)
    post_title = Column(Text, nullable=False)
    comment_text = Column(Text, nullable=False)
    language = Column(String(10), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow, nullable=False)
    processed_at = Column(TIMESTAMP, nullable=True)
    vector_embedding = Column(Text, nullable=True)  # Storing embeddings as a serialized string
    analysis_id = Column(String(36), ForeignKey("analysis_result.analysis_id"), nullable=True)

    def __str__(self) -> str:
        return (
            f"Comment(\n"
            f"  id={self.id},\n"
            f"  thread_id={self.thread_id},\n"
            f"  user_id={self.user_id},\n"
            f"  post_title={self.post_title},\n"
            f"  comment_text={self.comment_text},\n"
            f"  language={self.language},\n"
            f"  created_at={self.created_at},\n"
            f"  processed_at={self.processed_at},\n"
            f"  vector_embedding={self.vector_embedding},\n"
            f"  analysis_id={self.analysis_id}\n"
            f")"
        )