import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def ask(question, company, resume):
    prompt = f"Pretend you are in an interview for {company}. This is your resume information: {resume}. " + question
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    for k in response['choices']:
        return k['message']['content'].strip()

def write_to_file(response):
    # this code removes newlines
    response = ''.join([line for line in response.split('\n') if line.strip()])

    with open('response.txt', 'w') as file:
        file.write(response)
    return response

company_name = 'Apple'
prompt = 'What is your name?'

with open("resume_info.txt", "r") as file:
    # Read the contents of the file into the variable 'resume'
    resume = file.read()

# print(resume)

write_to_file(ask(prompt, 'Royal Bank of Canada', resume).strip())



