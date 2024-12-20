from google.api_core import retry
from typing import Mapping, Any, TypedDict

import enum
import google.generativeai as genai

# inner imports
from utils.file_processor import read_yaml
from utils.prompts import PROMPT, PROMPT_JSON_MODE

class Sentiment(enum.Enum):
    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"
    MIXED = "mixed"

class Topic(enum.Enum):
    PLAYER_PERFORMANCE = "Player Performance"
    GAME_OUTCOME = "Game Outcome"
    TEAM_STRATEGY = "Team Strategy"
    REFEREE_DECISIONS = "Referee Decisions"
    TRADES_RUMORS = "Trades/Rumors"
    INJURY_CONCERNS = "Injury Concerns"
    OFF_COURT_NEWS = "Off-Court News"
    GENERAL_DISCUSSION = "General Discussion"

class APIResponse(TypedDict):
    topic: Topic
    sentiment: Sentiment
    sentiment_score: float

class GeminiAPI:
    def __init__(self) -> None:
        pass

    def __init__(self, config: Mapping[str, Any]) -> None:
        self.set_api_key(config)
        self.set_api_config(config)
        self.create_model()

    def set_api_key(self, config: Mapping[str, Any]) -> None:
        try:
            genai.configure(api_key=config.get("GOOGLE_API_KEY"))
        except Exception as e:
            print(e)

    def set_api_config(self, config: Mapping[str, Any]) -> None:
        self.GENAI_CONFIG = genai.GenerationConfig(
            temperature=config.get("temperature", 1.0),
            top_k=config.get("top_k", 40),
            top_p=config.get("top_p", 0.95),
            # NOTE: JSON MODE is not as stable as few-shot mode
            # response_mime_type="application/json",
            # response_schema=list[APIResponse],
        )

        self.retry_policy = {"retry": retry.Retry(predicate=retry.if_transient_error)}

    def create_model(self) -> None:
        self.genai_model = genai.GenerativeModel(
            "gemini-1.5-flash",
            generation_config=self.GENAI_CONFIG
        )

    def send_prompt(self, post_tile: str, comment: str) -> str:
        return self.genai_model.generate_content(PROMPT.format(post_title=post_tile, comment=comment))

    def send_prompt_json_mode(self, post_title: str, comment: str) -> str:
        return self.genai_model.generate_content(PROMPT_JSON_MODE.format(post_title=post_title, comment=comment))

    def get_model_config(self) -> Mapping[str, Any]:
        return {
            "model_name": self.genai_model.model_name,
            "temperature": self.GENAI_CONFIG.temperature,
            "top_k": self.GENAI_CONFIG.top_k,
            "top_p": self.GENAI_CONFIG.top_p,
        }

def main():
    config = read_yaml("./etc/config.yaml")
    genai_api = GeminiAPI(config)

if __name__ == "__main__":
    main()

