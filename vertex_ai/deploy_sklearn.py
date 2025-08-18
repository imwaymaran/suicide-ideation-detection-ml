import os
from dotenv import load_dotenv
from google.cloud import aiplatform

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION   = os.getenv("LOCATION")
BUCKET     = os.getenv("BUCKET")
MODEL_ARTIFACT_URI = f"{BUCKET}/models/sklearn-1-5"
SERVING_IMAGE = "us-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-5:latest"

if __name__ == "__main__":
    aiplatform.init(project=PROJECT_ID, location=LOCATION)

    model = aiplatform.Model.upload(
        display_name="text-clf-sklearn",
        artifact_uri=MODEL_ARTIFACT_URI,
        serving_container_image_uri=SERVING_IMAGE
    )
    model.wait()

    endpoint = aiplatform.Endpoint.create(display_name="text-clf-endpoint")
    endpoint.wait()

    model.deploy(
        endpoint=endpoint,
        machine_type="n1-standard-2",
        traffic_split={"0": 100}
    )

    print("Model deployed to endpoint:", endpoint.resource_name)