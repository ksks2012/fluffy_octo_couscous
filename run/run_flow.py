
from utils.api.basic import GenaiAPI
from utils.api.chat import GenaiChatAPI
from utils.file_processor import read_json, read_yaml

def run_genai_api():
    # TODO: Replace test file with crawler data
    data = read_json("./var/test.json")
    print(data)

    config = read_yaml("./etc/config.yaml")
    genai_api = GenaiAPI(config)

    for value in data:
        response = genai_api.send_prompt(value["translated_title"], value["translated_message"])
        print(response.text)

def run_genai_chat_api():
    # TODO: Replace test file with crawler data
    data = read_json("./var/test.json")
    print(data)

    config = read_yaml("./etc/config.yaml")
    genai_api = GenaiChatAPI(config)
    genai_api.start_chat()

    for value in data:
        response = genai_api.send_msg_to_chat(value["translated_title"], value["translated_message"])
        print(response.text)

if __name__ == "__main__":
    # run_genai_api()
    run_genai_chat_api()