from typing import Any, Mapping

import google.generativeai as genai

# inner imports
from utils.api.basic import GenaiAPI
from utils.prompts import INSTRUCTION

class GenaiChatAPI(GenaiAPI):
    def __init__(self, config: Mapping[str, Any]) -> None:
        super().__init__(config)

    def create_model(self) -> None:
        self.flash_model = genai.GenerativeModel(
            "gemini-1.5-flash",
            generation_config=self.GENAI_CONFIG,
            system_instruction=INSTRUCTION
        )

    def start_chat(self) -> str:
        # TODO: Implement function call for reading history message of account from DB 
        return self.flash_model.start_chat()

    def send_msg_to_chat(self, post_title: str, comment: str) -> str:
        return self.flash_model.send_message(comment, retry_policy=self.retry_policy)