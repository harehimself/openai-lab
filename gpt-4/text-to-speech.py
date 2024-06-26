## Generate spoken audio from input text
import openai
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()
##from pathlib import Path
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Today is a wonderful day to build something people love!",
)

response.stream_to_file(speech_file_path)

## By default, the endpoint will output a MP3 file of the spoken audio but it can also be configured to output any of our supported formats.
