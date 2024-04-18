from flask import Flask, render_template
import subprocess
app = Flask(__name__, template_folder='templates')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/runcode')
def run_code():
    subprocess.Popen(["python", "main.py"])
    return 'turning the camera on'

if __name__ == '__main__':
    app.run(debug=True)
