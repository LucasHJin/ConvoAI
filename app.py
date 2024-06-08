from flask import Flask, render_template

app = Flask(__name__)

def read_file(filepath):
    with open(filepath, 'r') as file:
        return [line.strip() for line in file.readlines()]

@app.route('/')
def index():
    questions = read_file('q_output.txt')
    answers = read_file('a_output.txt')
    qa_pairs = zip(questions, answers)
    return render_template('index.html', qa_pairs=qa_pairs)


if __name__ == '__main__':
    extra_files = ['./a_output.txt', './q_output.txt']
    app.run(debug=True, extra_files=extra_files)