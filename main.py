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

user_question = input("Your Question: ")

prompt = f"""
{JSON_SYSTEM_PROMPT}

Question:

{user_question}
"""

response = ask_gemini(prompt)

print(response)