from typing import Mapping, Any, TypedDict

import enum
import google.generativeai as genai

from utils.file_processor import read_yaml

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


PROMPT = """
    You are an advanced text classifier for analyzing basketball forum discussions. Given a post title and a comment, identify the topic and sentiment of the comment. Return the result in JSON format.

### Guidelines:
1. The "topic" should describe the primary subject of the comment. Select from:
   - "Player Performance"
   - "Game Outcome"
   - "Team Strategy"
   - "Referee Decisions"
   - "Trades/Rumors"
   - "Injury Concerns"
   - "Off-Court News"
   - "General Discussion"
2. The "sentiment" should describe the emotional tone of the comment. Select from:
   - "Positive"
   - "Negative"
   - "Neutral"
   - "Mixed"
3. Optionally include a "sentiment_score" field with a value between 0.0 and 1.0, where higher values indicate stronger sentiment.

### Input:
- Post Title: {post_title}
- Comment: {comment}

### Output:
Return the classification result in the following JSON format:
```json
{{
  "topic": "<topic>",
  "sentiment": "<sentiment>",
  "sentiment_score": <sentiment_score>
}}
"""

PROMPT_JSON_MODE = """
    You are an advanced text classifier for analyzing basketball forum discussions. Given a post title and a comment, identify the topic and sentiment of the comment. Return the result in JSON format.

### Input:
- Post Title: {post_title}
- Comment: {comment}
### Output:
Return the classification result in the following JSON format:
```json
{{
  "topic": "<topic>",
  "sentiment": "<sentiment>",
  "sentiment_score": <sentiment_score>
}}
"""


class GenaiAPI:
    def __init__(self) -> None:
        pass

    def __init__(self, config: Mapping[str, Any]) -> None:
        self.set_api_key(config)
        self.set_api_config(config)

    def set_api_key(self, config: Mapping[str, Any]) -> None:
        try:
            genai.configure(api_key=config.get("GOOGLE_API_KEY"))
        except Exception as e:
            print(e)

    def set_api_config(self, config: Mapping[str, Any]) -> None:
        GENAI_CONFIG = genai.GenerationConfig(
            temperature=config.get("temperature", 1.0),
            top_k=config.get("top_k", 64),
            top_p=config.get("top_p", 0.95),
            # NOTE: JSON MODE is not as stable as few-shot mode
            # response_mime_type="application/json",
            # response_schema=list[APIResponse],
        )
        self.flash_model = genai.GenerativeModel(
            config.get("model_name", "gemini-1.5-flash"),
            generation_config=GENAI_CONFIG
        )

    def send_prompt(self, post_tile: str, comment: str) -> str:
        return self.flash_model.generate_content(PROMPT.format(post_title=post_tile, comment=comment))

    def send_prompt_json_mode(self, post_tile: str, comment: str) -> str:
        return self.flash_model.generate_content(PROMPT_JSON_MODE.format(post_title=post_tile, comment=comment))

def main():
    config = read_yaml("./etc/config.yaml")
    genai_api = GenaiAPI(config)

if __name__ == "__main__":
    main()

