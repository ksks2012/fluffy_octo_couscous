from sqlalchemy import Column, String, Text, Integer, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
import uuid

from internal.dao import Base

class SearchLog(Base):
    __tablename__ = 'search_log'

    search_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    query_text = Column(Text, nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False)
    result_count = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<SearchLog(search_id={self.search_id}, query_text={self.query_text}, timestamp={self.timestamp}, result_count={self.result_count})>"