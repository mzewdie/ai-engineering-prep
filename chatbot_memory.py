from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(api_key=api_key)

history = []

print("Gemini Chatbot")
print("Type 'quit' to exit.\n")

while True:
    prompt = input("You: ")

    if prompt.lower() == "quit":
        break

    history.append(f"User: {prompt}")

    conversation = "\n".join(history)

    try:
        print("\n--- Conversation Sent To Gemini ---")
        print(conversation)
        print("-----------------------------------\n")
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=conversation
        )

        answer = response.text

        print("\nGemini:")
        print(answer)
        print()

        history.append(f"Assistant: {answer}")

    except Exception as e:
        print(f"\nError: {e}\n")