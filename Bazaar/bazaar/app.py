from flask import Flask, send_from_directory, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Path to the directory containing files
BASE_DIR = 'files'  # Base directory for file downloads
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}  # Allowed file types
PASSWORD = "your_password"  # Set your desired password here

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return redirect(url_for('list_directory', path=''))

@app.route('/files/<path:path>')
def list_directory(path):
    full_path = os.path.join(BASE_DIR, path)
    items = os.listdir(full_path)
    return render_template('index.html', items=items, current_path=path)

@app.route('/files/<path:filename>')
def download_file(filename):
    full_path = os.path.join(BASE_DIR, filename)
    if not allowed_file(filename):
        return "File type not allowed.", 403
    return send_from_directory(BASE_DIR, filename)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        if password == PASSWORD:
            return redirect(url_for('index'))
    return '''
        <form method="post">
            Password: <input type="password" name="password">
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)