import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/')
def request_handler():
    print("received request")
    value = blocking()
    subprocess.Popen('python async.py foo 123', shell=True)
    print("responding")
    return value

def blocking():
    print("blocking")
    return "some value"

# Must be after routes are defined
if __name__ == '__main__':
    app.run(port=8000)
