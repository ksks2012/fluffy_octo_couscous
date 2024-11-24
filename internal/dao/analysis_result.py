from sqlalchemy import (
    Column,
    String,
    Text,
    Float,
    Integer,
)

import hashlib
import uuid

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
    hash_value = Column(String(64), unique=True, nullable=False)

    # Note: hash_value is generated from the following fields:
    # model_name, temperature, top_k, top_p, prompt
    def generate_hash(self) -> str:
        unique_string = f"{self.model_name}{self.temperature}{self.top_k}{self.top_p}{self.prompt}"
        return hashlib.sha256(unique_string.encode()).hexdigest()