from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

MODEL = "gpt-4o"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1 - Basic Chat

completion = client.chat.completions.create(
  model=MODEL,
  messages=[
    {"role": "system", "content": "You are a helpful assistant. Help me with my math homework!"},
    {"role": "user", "content": "Hello! Could you solve 2+2?"}
  ]
)

print("Assistant: " + completion.choices[0].message.content)

