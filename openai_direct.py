# Same as index.py, but using the plain OpenAI library against the Foundry
# resource's OpenAI-compatible endpoint. This talks to the model deployment
# directly, so it does NOT use the "andresgpt" agent's instructions/tools.

import os

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # reads .env in the project root (see .env.example)

base_url = os.environ["AZURE_OPENAI_BASE_URL"]
deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # deployment name, not model name
user_message = "Hi andresgpt"  # name example

# Auth via your `az login` session (no API key). To use a key instead,
# replace token_provider with the key string from the Foundry portal.
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

client = OpenAI(base_url=base_url, api_key=token_provider)

response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": user_message}],
)

print(f"Response output: {response.output_text}")
