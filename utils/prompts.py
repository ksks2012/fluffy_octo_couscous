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

