import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()


class VisionService:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is not configured."
            )

        self.client = genai.Client(
            api_key=api_key
        )

        self.model = "gemini-3.6-flash"

    def analyze_image(self, image_path, prompt):

        with open(image_path, "rb") as file:

            image_bytes = file.read()

        response = self.client.models.generate_content(

            model=self.model,

            contents=[

                prompt,

                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type="image/png"
                )
            ]
        )

        return response.text