import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/')
def request_handler():
    print("received request")
    value = blocking()
    subprocess.Popen('python async.py', shell=True)
    print("responding")
    return value

def blocking():
    print("blocking")
    return "some value"
