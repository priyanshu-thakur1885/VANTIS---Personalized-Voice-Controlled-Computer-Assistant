import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from core.tools_schema import TOOLS


load_dotenv()


class AIService:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is not configured."
            )

        self.client = genai.Client(
            api_key=api_key
        )

    def ask(self, message):

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=message,
        )

        return response.text

    def process(self, user_message):

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",

            contents=user_message,

            config=types.GenerateContentConfig(
                system_instruction="""
You are Vantis, a computer-use AI assistant.

Your job is to understand the user's request
and use the available tools when necessary.

Never pretend that an action was completed
unless the corresponding tool was actually called.

Use the smallest number of tools necessary.

Do not execute destructive or dangerous actions
without confirmation.
""",

                tools=TOOLS
            )
        )

        return response