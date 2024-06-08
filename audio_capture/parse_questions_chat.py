import openai
import os
from dotenv import load_dotenv
load_dotenv()
import text_answers

openai.api_key = os.getenv('OPENAI_API_KEY')

with open('txt/output.txt', 'r') as file:
    text = file.read()
    
def ask(text):
    if text.strip() != '':
        print("This is what text looks like", text)
        prompt = f"This is the a line of statements and questions from an interviewer that does not contain capitalization or punctuation: {text} Determine all the questions found within the text (precisely as written). However, if there are words you think are mispelt or should be replaced by a different word, you are able to switch out those individual words. Additionally, if there are parts of a question but the question seems unfinished (i.e. 'how is...' or 'don't you'), don't include them in the response. Also, include more unconventional questions such as 'Explain...' or 'State...'. Within the response, provide it exactly as written (other than your objective judgments as stated before) without capitalization or punctuation or any additional unnecessary words such as 'so the...'. Provide each individually identified question on a new line without any extra white space, numbers or any other characters on either side."

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        for k in response['choices']:
            return k['message']['content'].strip().split('\n')
    return

with open("./txt/resume_info.txt", "r") as file:
    # Read the contents of the file into the variable 'resume'
    resume = file.read()

response = ask(text)


with open("./txt/q_output.txt", "w") as file:
    if response != None and response != '':
        for i in response:
            file.write(i)
            file.write('\n')
            if i != '':
                print(i, "blah")
                text_answers.write_to_file(text_answers.ask(i, text_answers.company, resume))
