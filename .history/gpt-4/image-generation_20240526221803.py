## Generate an image.
import openai
from dotenv import load_dotenv
import os


from openai import OpenAI

# Load the .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url


## Edit an image.
from openai import OpenAI
client = OpenAI()

response = client.images.edit((
  model="dall-e-2",
  image=open("sunlit_lounge.png", "rb"),
  mask=open("mask.png", "rb"),
  prompt="A sunlit indoor lounge area with a pool containing a flamingo",
  n=1,
  size="1024x1024"
)
image_url = response.data[0].url


## Generate a variation of an image.
from openai import OpenAI
client = OpenAI()

response = client.images.create_variation(
  image=open("image_edit_original.png", "rb"),
  n=2,
  size="1024x1024"
)

image_url = response.data[0].url

## The Python examples in the guide above use the open function to read image data from disk. In some cases, you may have your image data in memory instead. Here's an example API call that uses image data stored in a BytesIO object:
from io import BytesIO
from openai import OpenAI
client = OpenAI()

## This is the BytesIO object that contains your image data
byte_stream: BytesIO = [your image data]
byte_array = byte_stream.getvalue()
response = client.images.create_variation(
  image=byte_array,
  n=1,
  model="dall-e-2",
  size="1024x1024"
)

## It may be useful to perform operations on images before passing them to the API. Here's an example that uses PIL to resize an image:
from io import BytesIO
from PIL import Image
from openai import OpenAI
client = OpenAI()

## Read the image file from disk and resize it
image = Image.open("image.png")
width, height = 256, 256
image = image.resize((width, height))

## Convert the image to a BytesIO object
byte_stream = BytesIO()
image.save(byte_stream, format='PNG')
byte_array = byte_stream.getvalue()

response = client.images.create_variation(
  image=byte_array,
  n=1,
  model="dall-e-2",
  size="1024x1024"
)

## Error Handling
import openai
from openai import OpenAI
client = OpenAI()

try:
  response = client.images.create_variation(
    image=open("image_edit_mask.png", "rb"),
    n=1,
    model="dall-e-2",
    size="1024x1024"
  )
  print(response.data[0].url)
except openai.OpenAIError as e:
  print(e.http_status)
  print(e.error)