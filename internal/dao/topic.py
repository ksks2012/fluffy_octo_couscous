from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

from internal.dao import Base

class Topic(Base):
    __tablename__ = 'topic'

    topic_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    topic_name = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<Topic(topic_id={self.topic_id}, topic_name={self.topic_name})>"