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

#response = ask_gemini(prompt)

""" chatbot1 = Chatbot()
chatbot1.add_message("I am chatbot1")
print(f"History in Chatbot1: {chatbot1.show_history()}")

chatbot2= Chatbot()
chatbot2.add_message("I am chatbot2")
print(f"History in Chatbot2: {chatbot2.show_history()}") """

bot = Chatbot(JSON_SYSTEM_PROMPT)
#response = bot.ask(prompt)



while True:
    question = input("Your Question: ")

    if question.lower() == "quit":
        break

    answer = bot.ask(question)

    print("\nGemini:")

    print(answer)

    print()
    #bot.show_history()



#print(response)