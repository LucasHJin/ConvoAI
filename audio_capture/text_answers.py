import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
model = "gpt-4o"
# USE FOR DEMO
# model = "gpt-4o"

def erase_file():
    with open("./txt/response.txt", "w") as f:
        pass

def ask(question, company, resume):
    prompt = f"Pretend you are in an interview for {company}. This is your resume information: {resume}. Only mention aspects from the resume if necessary. For technical questions, you do not need to mention the resume. Answer in first person, using jot-notes, don't add any extra characters such as asterisks or hashtags for the purpose of bolding, italicizing, etc. Only include the most pertninent information that directly answers the question and don't try to answer other questions. " + question
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    for k in response['choices']:
        return k['message']['content'].strip()

def write_to_file(response):
    # print(response)
    # this code removes newlines
    # response = ''.join([line for line in response.split('\n') if line.strip()])
    with open('./txt/response.txt', 'a') as file:
        file.write(response)
        file.write('\n!!!\n')
    return response

# erase_file()

# # clear response.txt
# with open("./txt/response.txt", "w") as file: 1

company = 'ERROR!'
resume = 'ERROR!'
with open("./txt/resume_info.txt", "r") as file:
    # Read the contents of the file into the variable 'resume'
    resume = file.read()
with open("./company.txt", "r") as file:
    company = file.read()
# with open("./txt/q_output.txt", "r") as file:
#     q = file.read().split('\n')[-1]
#     write_to_file(ask(q, company, resume))