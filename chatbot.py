from gemini_client import ask_gemini
from prompts import JSON_SYSTEM_PROMPT

class Chatbot:

    def __init__(self, system_prompt):
        self.system_prompt = system_prompt
        self.history = []

    def add_message(self, message):
        #print(f"Adding message {message}")
        self.history.append(message)

    def show_history(self):
        print("Printing content of history...")
        for message in self.history:
            print(message)
            
    def ask(self, question, task_prompt=""):
        self.history.append(f"User: {question}")
        prompt = self._build_prompt(task_prompt)
        print(f"User Asking with the prompt: {prompt}")
        answer = ask_gemini(prompt)
        self.history.append(f"Gemini: {answer}")
        return answer
    
    def _build_prompt(self, question, task_prompt=""):

        conversation = "\n".join(self.history)
        
        return f"""
        {self.system_prompt}

        {task_prompt}

        Conversation:

        {conversation}

        User:

        {question}
        """