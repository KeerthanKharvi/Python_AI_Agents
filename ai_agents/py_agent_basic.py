import requests
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get the API key
api_key = os.getenv("GROQ_API_KEY")

def query_groq_api(model: str, system_content: str,user_query: str):
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": system_content
            },
            {
                "role": "user",
                "content": user_query
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    # error handling
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Request failed: {response.status_code} - {response.text}")


# Defining the LLM Persona
system_content="You're an expert in building AI Agents using Python"

#User query
user_query="How to effectively build AI Agents using LLM"
# Example usage
response_data = query_groq_api(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    system_content=system_content,
    user_query=user_query
)

# Print the assistant's reply
print(response_data['choices'][0]['message']['content'])
