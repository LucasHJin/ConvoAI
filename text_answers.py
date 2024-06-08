import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
model = "gpt-3.5-turbo"
# USE FOR DEMO
# model = "gpt-4o"

def ask(question, company, resume):
    prompt = f"Pretend you are in an interview for {company}. This is your resume information: {resume}. Answer in first person, using jot-notes and only include the most pertninent information. " + question
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    for k in response['choices']:
        return k['message']['content'].strip()

def write_to_file(response):
    print(response)
    # this code removes newlines
    # response = ''.join([line for line in response.split('\n') if line.strip()])

    with open('response.txt', 'a') as file:
        file.write(response)
        file.write('\n!!!\n')
    return response

# clear response.txt
with open("response.txt", "w") as file: 1

company = 'RBC'
resume = 'ERROR!'
with open("resume_info.txt", "r") as file:
    # Read the contents of the file into the variable 'resume'
    resume = file.read()

with open("q_output.txt", "r") as file:
    questions = file.read().split('\n')
    for q in questions:
        write_to_file(ask(q, company, resume))




