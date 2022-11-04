##################################################
####  OPENAI GPT-3 API: COMPLETIONS
##################################################

import requests
import Config
import openai

API_KEY = Config.api_key

openai.api_key = API_KEY

prompt = "Write a tagline for an ice cream shop."

response = openai.Completion.create(
    engine = "text-davinci-001", 
    prompt = prompt, 
    max_tokens = 10
)

print(response)