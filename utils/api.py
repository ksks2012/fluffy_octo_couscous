from typing import Mapping, Any

import enum
import google.generativeai as genai

from utils.file_processor import read_yaml

class Sentiment(enum.Enum):
    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"

class Topic(enum.Enum):
    PLAYERS = "players"
    TEAMS = "teams"
    GAMES = "games"

class GenaiAPI:
    def __init__(self) -> None:
        pass

    def __init__(self, config: Mapping[str, Any]) -> None:
        self.set_api_key(config)
        self.set_api_config(config)

    def set_api_key(self, config: Mapping[str, Any]) -> None:
        genai.configure(api_key=config.GOOGLE_API_KEY)

    def set_api_config(self, config: Mapping[str, Any]) -> None:
        GENAI_CONFIG = genai.GenerationConfig(
            temperature=config.get("temperature", 1.0),
            top_k=config.get("top_k", 64),
            top_p=config.get("top_p", 0.95),
            response_mime_type="text/x.enum",
            response_schema=Sentiment
        )
        self.flash_model = genai.GenerativeModel(
            'gemini-1.5-flash',
            model_config=GENAI_CONFIG
        )

def main():
    config = read_yaml("config.yaml")
    genai_api = GenaiAPI(config)

if __name__ == "__main__":
    main()

