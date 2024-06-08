from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

def read_file(filepath):
    with open(filepath, 'r') as file:
        return [line.strip() for line in file.readlines()]

@app.route('/')
def index():
    questions = read_file('q_output.txt')
    answers = read_file('response.txt')
    qa_pairs = zip(questions, answers)
    return render_template('index.html', qa_pairs=qa_pairs)

if __name__ == '__main__':
    extra_files = ['./a_output.txt', './response.txt']
    app.run(debug=True, extra_files=extra_files)