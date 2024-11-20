# Introduction

System for analyzing NBA basketball forum messages.

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
