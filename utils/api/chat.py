from typing import Any, Mapping

import google.generativeai as genai

# inner imports
from utils.api.basic import GenaiAPI
from utils.prompts import INSTRUCTION, PROMPT_CHAT_MODE

class GenaiChatAPI(GenaiAPI):
    def __init__(self, config: Mapping[str, Any]) -> None:
        super().__init__(config)
        self.chat = None

    def create_model(self) -> None:
        self.genai_model = genai.GenerativeModel(
            "gemini-1.5-flash",
            generation_config=self.GENAI_CONFIG,
            system_instruction=INSTRUCTION
        )

    def start_chat(self) -> str:
        # TODO: Implement function call for reading history message of account from DB 
        try:
            self.chat = self.genai_model.start_chat()
            return "Chat started"
        except Exception as e:
            print(e)
            return "Chat failed to start"

    def send_msg_to_chat(self, post_title: str, comment: str) -> str:
        response = ""
        if self.chat is None:
            return response
        try:
            response = self.chat.send_message(PROMPT_CHAT_MODE.format(post_title=post_title, comment=comment), request_options=self.retry_policy)
        except Exception as e:
            print(e)
        return response