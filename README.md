# Introduction

System for analyzing NBA basketball forum messages.

 # Command

 ## Alembic

-  Revision
  ```
  alembic revision --autogenerate -m <Message>
  ```

- Migrate
  ```
  alembic upgrade head
  ```

- Downgrade
  ```
  alembic downgrade <revision_id>
  ```

- Info
  ```
  alembic history
  ```


# To-Do List

- [ ] **Crawler**  
  - Collect forum comments using web scraping or APIs (e.g., Reddit's `r/nba`, Twitter, or specialized basketball forums).

- [ ] **Pre-processor**  
  - Clean the text data by:
    - Removing duplicate comments and meaningless symbols.
    - Handling emojis and multilingual content.

- [ ] **Text Analysis**  
  - Perform sentiment analysis using the **Gemini model** or similar large language models:
    - Classify sentiments into positive, negative, or neutral categories.
  - Expand sentiment analysis to support specific basketball-related topics, such as:
    - **Player Performance** (e.g., “LeBron James performance”).
    - **Game Controversies** (e.g., “referee decisions”).
    - **Team Strategies** (e.g., “defensive strategy”).

- [ ] **Database**  
  - Use **Vector Search** (e.g., FAISS or Pinecone) to convert comments into vectors for multilingual analysis.

- [ ] **Search**  
  - Build a query functionality allowing users to search comments by topic (e.g., specific teams or players).

- [ ] **UI**  
  - Automatically generate summary reports using models:
    - Identify popular topics (e.g., “trade rumors” or “team status”).
    - Display sentiment distribution (e.g., the ratio of positive and negative comments about a player).
    - Analyze trends over time (e.g., discussion heatmap).
  - Visualize analysis results:
    - Sentiment trend graphs.
    - Heatmaps or word clouds for trending topics.


# Feature and Structure

## Data Collection and Preprocessing
1. Collect forum comments using web scraping or APIs (e.g., Reddit's `r/nba`, Twitter, or specialized basketball forums).
2. Clean the text data by:
   - Removing duplicate comments and meaningless symbols.
   - Handling emojis and multilingual content.

## Text Analysis and Sentiment Classification
3. Perform sentiment analysis using the **Gemini model** or similar large language models:
   - Classify sentiments into positive, negative, or neutral categories.
4. Expand sentiment analysis to support specific basketball-related topics, such as:
   - **Player Performance** (e.g., “LeBron James performance”).
   - **Game Controversies** (e.g., “referee decisions”).
   - **Team Strategies** (e.g., “defensive strategy”).

## Embedding and Multilingual Support
5. Use **Vector Search** (e.g., FAISS or Pinecone) to convert comments into vectors for multilingual analysis.
6. Build a query functionality allowing users to search comments by topic (e.g., specific teams or players).

## Insight Report Generation
7. Automatically generate summary reports using models:
   - Identify popular topics (e.g., “trade rumors” or “team status”).
   - Display sentiment distribution (e.g., the ratio of positive and negative comments about a player).
   - Analyze trends over time (e.g., discussion heatmap).
8. Visualize analysis results:
   - Sentiment trend graphs.
   - Heatmaps or word clouds for trending topics.

# Database Structure Design

## 1. Comments Table
Stores the original forum titles and comments, along with the API's classification and sentiment analysis results.

| **Column Name**      | **Type**         | **Description**                                                       |
|-----------------------|------------------|------------------------------------------------------------------------|
| `id`                 | `UUID`           | Unique identifier for each comment.                                   |
| `thread_id`          | `UUID`           | Unique identifier for the discussion thread.                          |
| `user_id`            | `VARCHAR(50)`    | Identifier for the user who posted the comment.                       |
| `post_title`         | `TEXT`           | The title of the forum discussion.                                    |
| `comment_text`       | `TEXT`           | The content of the comment.                                           |
| `topic`              | `VARCHAR(50)`    | Topic classification of the comment (e.g., "Player Performance").     |
| `sentiment`          | `VARCHAR(20)`    | Sentiment classification (e.g., "Positive", "Negative").              |
| `sentiment_score`    | `FLOAT`          | Sentiment intensity score (range 0.0 - 1.0).                          |
| `language`           | `VARCHAR(10)`    | The language of the comment (e.g., "en", "zh").                       |
| `created_at`         | `TIMESTAMP`      | Original publication timestamp of the comment.                        |
| `processed_at`       | `TIMESTAMP`      | Timestamp when the API analysis was completed.                        |
| `vector_embedding`   | `VECTOR`         | Vector embedding for multilingual search and similarity matching.     |

---

## 2. Topics Table
Stores all known topic categories to support topic classification queries.

| **Column Name**      | **Type**       | **Description**                           |
|-----------------------|----------------|-------------------------------------------|
| `topic_id`           | `UUID`         | Unique identifier for each topic.         |
| `topic_name`         | `VARCHAR(50)`  | Name of the topic (e.g., "Player Performance"). |

---

## 3. Search Logs Table
Records user search history to analyze popular topics or sentiment trends.

| **Column Name**      | **Type**         | **Description**                           |
|-----------------------|------------------|-------------------------------------------|
| `search_id`          | `UUID`           | Unique identifier for each search.        |
| `query_text`         | `TEXT`           | User's search keywords.                   |
| `timestamp`          | `TIMESTAMP`      | Timestamp of the search.                  |
| `result_count`       | `INTEGER`        | Number of results returned by the search. |

# Issue

- Duplicate Comments
- Multilingual text processing difficulty