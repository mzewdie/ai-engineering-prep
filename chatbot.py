from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(api_key=api_key)

print("Gemini Chatbot")
print("Type 'quit' to exit.\n")

while True:
    prompt = input("You: ")

    if prompt.lower() == "quit":
        break
    
    print(f"User question is: {prompt}")
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("\nGemini:")
        print(response.text)
        print()

    except Exception as e:
        #print(f"\nError: {e}\n")
        print(type(e))
        print(e)

    print("\nGemini:")
    print(response.text)
    print()