from bs4 import BeautifulSoup
from typing import Any, Mapping

from utils.file_processor import write_json

def process_ptt_html(soup: BeautifulSoup) -> Mapping[str, Any]:
    # Extract post title
    meta_lines = soup.find_all("div", class_="article-metaline")
    post_title = None
    for meta in meta_lines:
        if meta.find("span", class_="article-meta-tag").text.strip() == "標題":
            post_title = meta.find("span", class_="article-meta-value").text.strip()
            break

    # Extract post content
    post_content = soup.find(id="main-content").get_text().split("--")[0].strip()

    # Extract comments
    comments = []
    for push in soup.find_all("div", class_="push"):
        user_id = push.find("span", class_="push-userid").text.strip()
        comment_text = push.find("span", class_="push-content").text.strip(": ").strip()
        comments.append({"user_id": user_id, "comment_text": comment_text})

    # Organize into dictionary
    data = {
        "post_title": post_title,
        "post_content": post_content,
        "comments": comments
    }

    # Print result
    print(data)

    write_json("var/M.1732505498.A.54D.json", data)

    return data
