'''
Text Analysis Example
Heavily based on: https://microsoftlearning.github.io/mslearn-ai-fundamentals/Instructions/Exercises/03b-text-analysis.html#use-a-specialized-language-analysis-tool
'''
import os
from dotenv import load_dotenv

load_dotenv()

endpoint = os.environ["AZURE_TEXTANALYSIS_ENDPOINT"]

# !! This is different from MLearn's proper documentation since we're using Microsoft EntraID instead of just endpoint + key.
from azure.ai.textanalytics import TextAnalyticsClient
from azure.identity import DefaultAzureCredential

with (
    DefaultAzureCredential() as credential,
    TextAnalyticsClient(
        endpoint=endpoint,
        credential=credential,
        allow_preview=True,
    ) as project_client,
):
        
    # Example method for detecting sensitive information (PII) from text
    def pii_recognition_example(client):
        documents = [
            "Call Jane Doe at 555-123-4567 or email jane.doe@example.com."
        ]
        response = client.recognize_pii_entities(documents, language="en")
        result = [doc for doc in response if not doc.is_error]
        for doc in result:
            print("Redacted Text: {}".format(doc.redacted_text))
            for entity in doc.entities:
                print("Entity: {}".format(entity.text))
                print(" Category: {}".format(entity.category))
                print(" Confidence Score: {}".format(entity.confidence_score))
                print(" Offset: {}".format(entity.offset))
                print(" Length: {}".format(entity.length))
    pii_recognition_example(project_client)