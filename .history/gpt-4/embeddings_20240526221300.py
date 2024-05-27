import openai
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Get your OpenAI API key from the .env file
openai.api_key = os.getenv('OPENAI_API_KEY')

# Text for which you want to create an embedding
text = "Transformers are models that process data in parallel."

# Create an embedding
response = openai.Embedding.create(
    input=text,
    engine="text-similarity-babbage-001",  # You can choose a different engine if needed
)

# Print the embedding
print(response["data"][0]["embedding"])