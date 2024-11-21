from sqlalchemy import Column, String, Text, Integer, TIMESTAMP
import uuid

from internal.dao import Base

class SearchLog(Base):
    __tablename__ = 'search_log'

    search_id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    query_text = Column(Text, nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False)
    result_count = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<SearchLog(search_id={self.search_id}, query_text={self.query_text}, timestamp={self.timestamp}, result_count={self.result_count})>"