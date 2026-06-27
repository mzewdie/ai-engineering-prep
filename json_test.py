from dotenv import load_dotenv
from google import genai
import os
import json

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(api_key=api_key)

history = []

print("Gemini Chatbot")
print("Type 'quit' to exit.\n")

while True:
    user_question = input("Your Question: ")

    if user_question.lower() == "quit":
        break

    full_prompt = f"""
You are an assistant.

Answer ONLY with valid JSON.

Use exactly this schema:

{{
    "language": "",
    "creator": "",
    "first_release": "",
    "summary": ""
}}

Question:

{user_question}

Do not write explanations.
Do not use markdown.
Do not surround the JSON with ```json.
Return only JSON.
"""

    history.append(f"User: {full_prompt}")

    conversation = "\n".join(history)

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=conversation
        )

        answer = response.text
        #alternative data = response.json()

        print("\nGemini: Answer in Json format:")
        print(answer)
        print()
        
        data = json.loads(answer)
        print(f"The response in python dictionary format is: {data}")
        print(f"Type of data is: {type(data)}")
        
        print("Accessing the fields:")
        print(data["language"])
        print(data["creator"])
        print(data.get("summary", "Summary not found!"))
        
        #back from python string to json
        json_string = json.dumps(data, indent=4)
        print("Converting again from dict to json:")
        print(json_string)

        history.append(f"Assistant: {answer}")
        
       
    except Exception as e:
        print(f"\nError: {e}\n")
    except json.JSONDecodeError as e:
        print("Invalid JSON received.")
        print(e)