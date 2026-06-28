from google import genai
from dotenv import load_dotenv
import os
from config import MODEL

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))



def ask_gemini(prompt):
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text