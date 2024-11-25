from time import sleep
import json

from utils.api.basic import GenaiAPI
from utils.api.chat import GenaiChatAPI
from utils.file_processor import read_json, read_yaml, write_json


def run_genai_api() -> None:
    # TODO: Replace test file with crawler data
    data = read_json("./var/test.json")
    print(data)

    config = read_yaml("./etc/config.yaml")
    genai_api = GenaiAPI(config)

    for value in data:
        response = genai_api.send_prompt(value["translated_title"], value["translated_message"])
        print(response.text)

def run_genai_chat_api() -> None:
    # TODO: Replace test file with crawler data
    data = read_json("./var/test.json")
    print(data)

    config = read_yaml("./etc/config.yaml")
    genai_api = GenaiChatAPI(config)
    genai_api.start_chat()

    for value in data:
        response = genai_api.send_msg_to_chat(value["translated_title"], value["translated_message"])
        print(response.text)

def run_genai_chat_api_loop():
    test_json = read_json("./var/M.1732505498.A.54D.json")
    post_title = test_json["post_title"]
    post_content = test_json["post_content"]
    comments = test_json["comments"]

    config = read_yaml("./etc/config.yaml")
    genai_api = GenaiChatAPI(config)
    genai_api.start_chat(post_title, post_content)

    response_list = []
    for comment in comments:
        comment_text = comment["comment_text"]
        try:
            response = genai_api.send_msg_to_chat(post_title, comment_text)
            print(response.text)
            tmp = response.text.replace("```json", "").replace("```", "").strip()
            print(tmp)
            response_list.append(json.loads(tmp))
        except Exception as e:
            print(e)
        sleep(5)

    write_json("var/response.json", response_list)

if __name__ == "__main__":
    run_genai_api()
    run_genai_chat_api()
    run_genai_chat_api_loop()