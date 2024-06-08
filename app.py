from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_socketio import SocketIO, emit
import os
import subprocess

app = Flask(__name__)
socketio = SocketIO(app)

def read_file(filepath):
    with open(filepath, 'r') as file:
        return [line.strip() for line in file.readlines()]

def read_file2(filepath):
    with open(filepath, 'r') as file:
        return [line for line in file.read().split('!!!')]

@app.route('/')
def index():
    questions = read_file('./txt/q_output.txt')
    answers = read_file2('./txt/response.txt')
    qa_pairs = zip(questions, answers)
    return render_template('index.html', qa_pairs=qa_pairs)

@app.route('/submit-resume', methods=['POST'])
def submit_resume():
    try:
        subprocess.Popen(["python", "./audio_capture/image_analysis.py"])
        return jsonify(success=True)
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/start-recording', methods=['POST'])
def start_recording():
    try:
        subprocess.Popen(["python", "./audio_capture/analyze_text.py"])
        subprocess.Popen(["python", "./audio_capture/voice_input.py"])
        subprocess.Popen(["python", "./audio_capture/text_answers.py"])
        subprocess.Popen(["python", "./audio_capture/parse.py"])
        return jsonify(success=True)
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/stop-recording', methods=['POST'])
def stop_recording():
    try:
        with open("stop.txt", "w") as f:
            pass  # create an empty stop file
        return jsonify(success=True)
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/upload', methods=['POST'])
def upload():
    folder_to_clear = 'uploads'

    clear_folder(folder_to_clear)

    if 'image' not in request.files:
        return 'No file part'

    file = request.files['image']

    if file.filename == '':
        return 'No selected file'

    file.save(os.path.join(folder_to_clear, file.filename))

    return redirect(url_for('index'))

def clear_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                clear_folder(file_path)
                os.rmdir(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

if __name__ == '__main__':
    socketio.run(app, debug=True)
