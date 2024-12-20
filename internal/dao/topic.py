from sqlalchemy import Column, String
import uuid

from internal.dao import Base

class Topic(Base):
    __tablename__ = 'topic'

    search_id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    topic_name = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<Topic(topic_id={self.topic_id}, topic_name={self.topic_name})>"