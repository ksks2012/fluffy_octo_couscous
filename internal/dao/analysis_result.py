from sqlalchemy import (
    Column,
    String,
    Text,
    Float,
    Integer,
)

import uuid
import datetime

from internal.dao import Base
class AnalysisResult(Base):
    __tablename__ = "analysis_result"

    analysis_id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
    sentiment = Column(String(20), nullable=False)
    sentiment_score = Column(Float, nullable=False)
    topic = Column(String(50), nullable=False)
    model_name = Column(String(100), nullable=False)
    temperature = Column(Float, nullable=True)
    top_k = Column(Integer, nullable=True)
    top_p = Column(Float, nullable=True)
    mode = Column(String(20), nullable=False)
    prompt = Column(Text, nullable=True)
