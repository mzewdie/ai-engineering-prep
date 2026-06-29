"""
    Architecture of the project:
    
    ai-engineering-prep/
│
├── .venv/
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
├── main.py
├── config.py
├── prompts.py
├── gemini_client.py
├── utils.py
│
├── chatbot.py        ← keep for now
├── json_test.py      ← keep for now
└── github_user.py    ← keep for now
    
    
"""

from gemini_client import ask_gemini
from prompts import JSON_SYSTEM_PROMPT
from chatbot import Chatbot

#user_question = input("Your Question: ")
user_question="wait"

prompt = f"""
{JSON_SYSTEM_PROMPT}

Question:

{user_question}
"""

bot = Chatbot(JSON_SYSTEM_PROMPT)

while True:
    question = input("Your Question: ")

    if question.lower() == "quit":
        break

    answer = bot.ask(question)

    print("\nGemini's Answer:")

    print(answer)

    #print()
 