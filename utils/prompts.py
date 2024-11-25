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

INSTRUCTION = """
You are a sophisticated language model specialized in analyzing basketball forum discussions. Your task is to classify comments into a topic and sentiment based on the context of the discussion thread's title. Follow these instructions precisely:

1. **Topic Classification**:
   - Determine the primary topic of the comment based on the provided post title and comment.
   - Available topics:
     - "Player Performance"
     - "Game Outcome"
     - "Team Strategy"
     - "Referee Decisions"
     - "Trades/Rumors"
     - "Injury Concerns"
     - "Off-Court News"
     - "General Discussion"

2. **Sentiment Classification**:
   - Assess the emotional tone of the comment.
   - Sentiments:
     - "Positive"
     - "Negative"
     - "Neutral"
     - "Mixed"
   - Optionally, provide a "sentiment_score" between 0.0 and 1.0 to indicate the strength of the sentiment (higher value = stronger emotion).

3. **Output Format**:
   - Always return the result in the following JSON format:
     ```json
     {
       "topic": "<topic>",
       "sentiment": "<sentiment>",
       "sentiment_score": <sentiment_score>
     }
     ```

4. **Be concise and ensure the classifications are relevant to basketball discussions.**

### Example Context:
- Post Title: "LeBron leads Lakers to victory in a thrilling game!"
- Comment: "LeBron's clutch performance in the fourth quarter was amazing, but the rest of the team needs to step up."

### Example Output:
```json
{
  "topic": "Player Performance",
  "sentiment": "Mixed",
  "sentiment_score": 0.75
}
"""

PROMPT_POST_CONTEXT = """
### Context:
You are analyzing comments from an online forum. Below is the content of the original post for reference. Use this to better understand the discussion.

- Post Title: {post_title}
- Post Content: {post_content}
"""


PROMPT_CHAT_MODE = """
### Input:
- Post Title: {post_title}
- Comment: {comment}
"""