from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
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

@app.route('/start-recording', methods=['POST'])
def start_recording():
    try:
        subprocess.Popen(["python", "./analyze_text.py"])
        subprocess.Popen(["python", "./voice_input.py"])
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
    # Specify the folder path you want to clear
    folder_to_clear = 'uploads'

    # Clear the folder
    clear_folder(folder_to_clear)

    # Check if the post request has the file part
    if 'image' not in request.files:
        return 'No file part'
    
    file = request.files['image']
    
    # If the user does not select a file, the browser submits an empty file without a filename
    if file.filename == '':
        return 'No selected file'

    # Save the file to the folder
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
    extra_files = ['./response.txt', './q_output.txt', './output.txt']
    app.run(debug=True, extra_files=extra_files)