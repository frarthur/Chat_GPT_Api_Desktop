import openai
from dotenv import load_dotenv
import os

class ChatController:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv('OPENAI_API_KEY')

    def get_response(self, user_input, model):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            return response.choices[0].message['content']
        except Exception as e:
            return f"Erreur : {str(e)}"
