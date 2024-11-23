import pytest
from unittest.mock import MagicMock
from utils.api.basic import GenaiAPI, Sentiment, Topic

@pytest.fixture
def genai_api():
    config = {
        "GOOGLE_API_KEY": "fake_api_key",
        "temperature": 0.7,
        "top_k": 50,
        "top_p": 0.9
    }
    return GenaiAPI(config)

def test_set_api_key(genai_api):
    genai_api.set_api_key({"GOOGLE_API_KEY": "new_fake_api_key"})
    assert genai_api.GENAI_CONFIG.temperature == 0.7
    assert genai_api.GENAI_CONFIG.top_k == 50
    assert genai_api.GENAI_CONFIG.top_p == 0.9

def test_set_api_config(genai_api):
    config = {
        "temperature": 0.8,
        "top_k": 60,
        "top_p": 0.85
    }
    genai_api.set_api_config(config)
    assert genai_api.GENAI_CONFIG.temperature == 0.8
    assert genai_api.GENAI_CONFIG.top_k == 60
    assert genai_api.GENAI_CONFIG.top_p == 0.85

def test_create_model(genai_api):
    genai_api.create_model()
    assert genai_api.genai_model is not None

def test_send_prompt(genai_api):
    genai_api.genai_model = MagicMock()
    genai_api.genai_model.generate_content.return_value = "generated_content"
    response = genai_api.send_prompt("Test Title", "Test Comment")
    assert response == "generated_content"

def test_send_prompt_json_mode(genai_api):
    genai_api.genai_model = MagicMock()
    genai_api.genai_model.generate_content.return_value = "generated_content_json"
    response = genai_api.send_prompt_json_mode("Test Title", "Test Comment")
    assert response == "generated_content_json"

def test_get_model_config(genai_api):
    config = genai_api.get_model_config()
    assert config["model_name"] == "models/gemini-1.5-flash"
    assert config["temperature"] == 0.7
    assert config["top_k"] == 50
    assert config["top_p"] == 0.9

if __name__ == "__main__":
    pytest.main()