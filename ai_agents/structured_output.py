import os

from groq import Groq
import openai
from dotenv import load_dotenv
from pydantic import BaseModel
import instructor

# Load the .env file
load_dotenv()

# Get the API key
api_key = os.getenv("GROQ_API_KEY_2")

client = instructor.from_groq(Groq(api_key=api_key), mode=instructor.Mode.JSON)

class ResearchText(BaseModel):
  instruction: str
  explanation: str

chat_completion =  client.chat.completions.create(
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
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    response_model = ResearchText
)

print(chat_completion)