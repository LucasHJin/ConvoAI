from flask_socketio import SocketIO, emit
from flask import Flask
import time

# Initialize SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

def read_file(filepath):
    with open(filepath, 'r') as file:
        return [line.strip() for line in file.readlines()]

def read_file2(filepath):
    with open(filepath, 'r') as file:
        return [line for line in file.read().split('!!!')]

def add_new_qa(question, answer):
    # Code to add Q&A pair to the files or database
    # ...
    socketio.emit('new_qa', {'question': question, 'answer': answer})

questions = read_file('./txt/q_output.txt')
answers = read_file2('./txt/response.txt')
qa_pairs = zip(questions, answers)
# Example of adding a Q&A pair
add_new_qa("Sample Question?", "Sample Answer!")
