import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def ask(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}],
        temperature=0.7
    )
    for k in response['choices']:
        return k['message']['content'].strip()

def write_to_file(response):
    # Write the response to response.txt
    with open('response.txt', 'w') as file:
        file.write(response)
    return response

company_name = 'Apple'
prompt = f'Pretend you are in an interview for {company_name}. What are your biggest weaknesses as an employee?'
write_to_file(ask(prompt))



