import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()  # reads .env in the project root (see .env.example)

endpoint = os.environ["AZURE_AI_PROJECT_ENDPOINT"]
agent_name = os.environ["AZURE_AI_AGENT_NAME"]
user_message = "Hi andresgpt" # name example

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(
        endpoint=endpoint,
        credential=credential,
        allow_preview=True,
    ) as project_client,
):
    # Bind the OpenAI client to the existing agent endpoint.
    # ?? It is actually a convention to use openai_client, as per the documentation
    openai_client = project_client.get_openai_client(agent_name=agent_name)

    # GitHub Copilot preview agents require a conversation for every Responses turn.
    conversation = openai_client.conversations.create()
    response = openai_client.responses.create(
        conversation=conversation.id,
        input=[{"role": "user", "content": user_message}],
        
        # !! In this case, it is unnecesary due to openai client already having a reference to the agent name.
        extra_body={'agent': {'name': agent_name, 'type': 'agent_reference'}}
    )

    print(f"Response output: {response.output_text}")