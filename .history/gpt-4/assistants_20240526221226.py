import openai
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

def openai_assistant(prompt):
    openai.api_key = os.getenv('OPENAI_API_KEY')  # Get the API key from the .env file
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or another model you prefer
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return str(e)

# Example usage
user_prompt = "Tell me about the history of the internet."
print(openai_assistant(user_prompt))
