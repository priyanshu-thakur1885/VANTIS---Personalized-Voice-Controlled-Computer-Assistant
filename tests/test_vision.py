from google import genai
from google.genai import types

import os
from dotenv import load_dotenv


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


with open("screen.png", "rb") as file:

    image_bytes = file.read()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[
        "Describe what is visible on this computer screen.",
        types.Part.from_bytes(
            data=image_bytes,
            mime_type="image/png"
        )
    ]
)


print(response.text)