import base64
import requests
import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
model = "gpt-3.5-turbo"
# USE FOR DEMO
# model = "gpt-4o"

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def analyze(image_path, prompt):
    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai.api_key}"
    }

    payload = {
    "model": model,
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": prompt
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 500
    }
    return requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload).json()

uploads_folder = 'uploads'
first_file = next(iter(os.listdir(uploads_folder)), None)
if first_file:
    file_path = os.path.join(uploads_folder, first_file)
# print(file_path)
response = analyze(file_path, "Summarize the main points of this resume.")
with open('resume_info.txt', 'w') as file:
    file.write(response["choices"][0]["message"]["content"])

