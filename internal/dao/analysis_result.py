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
    # FIXME: Add a unique constraint to the hash_value column
    def generate_hash(self) -> str:
        unique_string = f"{self.analysis_id}{self.model_name}{self.temperature}{self.top_k}{self.top_p}{self.prompt}"
        return hashlib.sha256(unique_string.encode()).hexdigest()
    
    def __str__(self) -> str:
        return (
            f"AnalysisResult(\n"
            f"  analysis_id={self.analysis_id},\n"
            f"  sentiment={self.sentiment},\n"
            f"  sentiment_score={self.sentiment_score},\n"
            f"  topic={self.topic},\n"
            f"  model_name={self.model_name},\n"
            f"  temperature={self.temperature},\n"
            f"  top_k={self.top_k},\n"
            f"  top_p={self.top_p},\n"
            f"  mode={self.mode},\n"
            # f"  prompt={self.prompt},\n"
            f"  hash_value={self.hash_value}\n"
            f")"
        )