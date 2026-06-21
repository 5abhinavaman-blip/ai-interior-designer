from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
from io import BytesIO

load_dotenv()

HF_API_TOKEN = os.getenv("HF_API_TOKEN")

client = InferenceClient(
    provider="hf-inference",
    api_key=HF_API_TOKEN
)

def generate_image(prompt):

    image = client.text_to_image(
        prompt,
        model="black-forest-labs/FLUX.1-schnell"
    )

    buffer = BytesIO()
    image.save(buffer, format="PNG")

    return buffer.getvalue()