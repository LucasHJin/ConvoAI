import PyPDF2
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
model = "gpt-4o"

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Example usage:
# pdf_path = 'lucasresume.pdf'
# text = extract_text_from_pdf(pdf_path)
# print(text)

# def summarize(text):
#     prompt = f"Summarize the main points of this resume: {text}"
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.7
#     )
#     for k in response['choices']:
#         return k['message']['content'].strip()

# print(summarize(text))