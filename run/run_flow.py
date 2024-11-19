
from utils.api.basic import GenaiAPI
from utils.translator import TranslatorZhTwToEn
from utils.file_processor import read_json, read_yaml

def run_genai_api():
    # TODO: Replace test file with crawler data
    data = read_json("./var/test.json")
    print(data)

    translator = TranslatorZhTwToEn()
    for value in data:
        # Translate title and message
        translated_title = translator.translate(value["title"])
        translated_message = translator.translate(value["message"])

        value["translated_title"] = translated_title
        value["translated_message"] = translated_message

    config = read_yaml("./etc/config.yaml")
    genai_api = GenaiAPI(config)

    for value in data:
        response = genai_api.send_prompt(value["translated_title"], value["translated_message"])
        print(response.text)

def run_genai_chat_api():
    pass

if __name__ == "__main__":
    run_genai_api()
    run_genai_chat_api()