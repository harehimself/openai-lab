## TRANSCRIBE AUDIO
import openai
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()
## The transcriptions API takes as input the audio file you want to transcribe and the desired output file format for the transcription of the audio. We currently support multiple input and output file formats.

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

audio_file = open("/path/to/file/audio.mp3", "rb")
transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file)

# By default, the response type will be json with the raw text included.

## The Audio API also allows you to set additional parameters in a request. For example, if you want to set the response_format as text, your request would look like the following:

from openai import OpenAI

client = OpenAI()

audio_file = open("speech.mp3", "rb")
transcript = client.audio.transcriptions.create(
    model="whisper-1", file=audio_file, response_format="text"
)

## TRANSLATION

from openai import OpenAI

client = OpenAI()

audio_file = open("/path/to/file/german.mp3", "rb")
transcript = client.audio.translations.create(model="whisper-1", file=audio_file)

## LONGER INPUTS
## By default, the Whisper API only supports files that are less than 25 MB. If you have an audio file that is longer than that, you will need to break it up into chunks of 25 MB's or less or used a compressed audio format. To get the best performance, we suggest that you avoid breaking the audio up mid-sentence as this may cause some context to be lost. One way to handle this is to use the PyDub open source Python package to split the audio:

from pydub import AudioSegment

song = AudioSegment.from_mp3("good_morning.mp3")

## PyDub handles time in milliseconds
ten_minutes = 10 * 60 * 1000

first_10_minutes = song[:ten_minutes]

first_10_minutes.export("good_morning_10.mp3", format="mp3")
