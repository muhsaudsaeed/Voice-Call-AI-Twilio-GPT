import openai
from dotenv import load_dotenv
import os

load_dotenv()

def bot_query(query):
    """Query the OpenAI API with the user's input"""
    openai.api_key = os.environ.get('OPENAI_API_KEY')

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": "You are a assistant who will respond on call. The caller will ask you questions and you will respond to them. You can also ask questions to the caller. Write short responses to the caller's questions."},
        {"role": "user", "content": f"{query}"},
    ]
    )
    print(response)
    return response['choices'][0]['message']['content']
