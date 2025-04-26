import os

from groq import Groq
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get the API key
api_key = os.getenv("GROQ_API_KEY")

client = Groq(
    api_key=api_key,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You're an expert ",
        },
        {
            "role": "user",
            "content": "Effective and error free way to setup text to sql ai agents using llm",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)