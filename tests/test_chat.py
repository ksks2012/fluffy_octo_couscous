import pytest
from google.generativeai.types import content_types
from unittest.mock import MagicMock

from utils.api.chat import GenaiChatAPI
from utils.prompts import INSTRUCTION

@pytest.fixture
def genai_chat_api():
    config = {
        "GOOGLE_API_KEY": "fake_api_key",
        "temperature": 0.7,
        "top_k": 50,
        "top_p": 0.9
    }
    genai_chat_api = GenaiChatAPI(config)
    # Mock the flash_model methods
    genai_chat_api.genai_model = MagicMock()
    genai_chat_api.genai_model.start_chat.return_value = "chat_started"
    genai_chat_api.genai_model.send_message.return_value = {
        "topic": "Game Outcome",
        "sentiment": "Negative",
        "sentiment_score": 0.8
    }
    return genai_chat_api

@pytest.fixture
def test_data():
    data = [
        {
            'date': '2021-01-01',
            'message': 'I really want the Pelicans to win! It’s a pity they couldn’t take it down.',
            'translated_message': 'I really want the Pelicans to win! It’s a pity they couldn’t take it down.',
            'title': '[BOX ] Lakers 104:99 Pelicans',
            'translated_title': '[BOX ] Lakers 104:99 Pelicans',
            'user': 'xxx'
        },
    ]
    return data

def test_create_model(genai_chat_api):
    # Test create_model method
    genai_chat_api.create_model()
    assert genai_chat_api.flash_model._system_instruction == content_types.to_content(INSTRUCTION)
    assert genai_chat_api.flash_model is not None

def test_api_start_chat(genai_chat_api):
    # Test start_chat method
    response = genai_chat_api.start_chat()
    assert response == "chat_started"

def test_send_msg_to_chat(genai_chat_api, test_data):
    # Test send_msg_to_chat method
    for value in test_data:
        response = genai_chat_api.send_msg_to_chat(value["translated_title"], value["translated_message"])
        assert response == {
            "topic": "Game Outcome",
            "sentiment": "Negative",
            "sentiment_score": 0.8
        }

if __name__ == "__main__":
    pytest.main()