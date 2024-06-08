import base64
import requests
import os
import openai
from dotenv import load_dotenv
import pdf_extract
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
# model = "gpt-3.5-turbo"
# USE FOR DEMO
model = "gpt-4o"

def erase_file():
    with open("./txt/resume_info.txt", "w") as f:
        pass

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

erase_file()
uploads_folder = 'uploads'
first_file = next(iter(os.listdir(uploads_folder)), None)
if first_file:
    file_path = os.path.join(uploads_folder, first_file)
    if file_path.lower().endswith('.pdf'):
        text = pdf_extract.extract_text_from_pdf(file_path)
        os.makedirs('./txt', exist_ok=True)
        with open('./txt/resume_info.txt', 'w', encoding='utf-8') as file:
            file.write(text)
    else:
        response = analyze(file_path, "Summarize the main points of this resume.")
        os.makedirs('./txt', exist_ok=True)
        with open('./txt/resume_info.txt', 'w', encoding='utf-8') as file:
            file.write(response["choices"][0]["message"]["content"])
else:
    print("No files found in the uploads folder.")
