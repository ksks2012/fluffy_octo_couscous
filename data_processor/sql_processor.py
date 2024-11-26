from typing import Any, Mapping, List, Tuple
from datetime import datetime, timezone
import uuid

from internal.dao.analysis_result import AnalysisResult
from internal.dao.comment import Comment

# TODO:
def process_comment(comment: Mapping[str, Any], post_title: str, analysis_id: str) -> Comment:
    return Comment(
        thread_id=str(uuid.uuid4()),
            user_id=comment["user_id"],
            post_title=post_title,
            comment_text=comment["comment_text"],
            language="zh-tw",
            created_at=datetime.now(timezone.utc),
            processed_at=datetime.now(timezone.utc),
            vector_embedding=None,
            analysis_id=analysis_id
        )


# TODO:
def process_analysis_result(config: Mapping[str, Any], comment: Mapping[str, Any]) -> AnalysisResult:
    """
        config
            model_name: str
            temperature: float
            top_k: int
            top_p: float
            mode: str
            prompt: str
        comments: List[
            {
                user_id: str
                comment_text: str
                analysis_result: {
                    topic: str
                    sentiment: str
                    sentiment_score: float
                }
            }
        ]
    """
    return AnalysisResult(
        analysis_id=str(uuid.uuid4()),
        sentiment=comment["analysis_result"]["sentiment"],
        sentiment_score=comment["analysis_result"]["sentiment_score"],
        topic=comment["analysis_result"]["topic"],
        model_name=config["model_name"],
        temperature=config["temperature"],
        top_k=config["top_k"],
        top_p=config["top_p"],
        mode=config["mode"],
        prompt=config["prompt"]
    )

def process_response(config: Mapping[str, Any], response: Mapping[str, Any]) -> Tuple[List[Comment], List[AnalysisResult]]:
    """
        config
            model_name: str
            temperature: float
            top_k: int
            top_p: float
            mode: str
            prompt: str
        response (After response)
            post_title: str
            post_content: str
            comments: List[
                {
                    user_id: str
                    comment_text: str
                    analysis_result: {
                        topic: str
                        sentiment: str
                        sentiment_score: float
                    }
                }
            ]
    """
    comment_lsit = []
    analysis_result_list = []

    for value in response["comments"]:
        # Process the analysis result 
        analysis_result = process_analysis_result(config, value)
        analysis_result_list.append(analysis_result)

        # Process the comment
        comment = process_comment(value, response["post_title"], analysis_result.analysis_id)
        comment_lsit.append(comment)


    return comment_lsit, analysis_result_list