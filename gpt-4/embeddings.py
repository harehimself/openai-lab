import openai

## Set your OpenAI API key
openai.api_key = OPENAI_API_KEY

## Text for which you want to create an embedding
text = "Transformers are models that process data in parallel."

## Create an embedding
response = openai.Embedding.create(
    input=text,
    engine="text-similarity-babbage-001",  ## You can choose a different engine if needed
)

## Print the embedding
print(response["data"][0]["embedding"])


## In this example, replace 'your-api-key' with your actual OpenAI API key, and you can modify the text variable with the content for which you want to create an embedding.

## The engine parameter specifies the model used for creating embeddings. There are different engines available, and you can choose one based on your requirements (like "text-similarity-babbage-001" in this example).
