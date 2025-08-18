import os
from dotenv import load_dotenv
from google.cloud import aiplatform

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION   = os.getenv("LOCATION")
ENDPOINT_ID = os.getenv("ENDPOINT_ID")

sample_texts = [
    "I feel trapped and hopeless.",
    "Had a good day at school and I’m excited for the weekend."
]

if __name__ == "__main__":
    aiplatform.init(project=PROJECT_ID, location=LOCATION)
    endpoint = aiplatform.Endpoint(endpoint_name=f"projects/{PROJECT_ID}/locations/{LOCATION}/endpoints/{ENDPOINT_ID}")

    preds = endpoint.predict(instances=sample_texts)
    print(preds.predictions)   