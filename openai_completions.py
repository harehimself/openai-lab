##################################################
##  OPENAI GPT-3 API: Completions
##################################################

import requests
import config
import openai

API_KEY = config.api_key

openai.api_key = API_KEY

prompt = "Write a tagline for an ice cream shop."

response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=6)

print(response)