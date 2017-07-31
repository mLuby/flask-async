# Flask Async
Flask (Python) server that allows non-blocking execution AFTER response returns.
It's hacky but it works (unlike asyncio 😡).

## Install (macOS)
```sh
brew install python3
pip3 install Flask
```

## Start
```sh
FLASK_APP=server.py /Library/Frameworks/Python.framework/Versions/3.6/bin/flask run
```
Browse to http://localhost:5000/

You will see messages printed in this order:
```
received request
blocking
responding
non-blocking with args ['foo' '123']
```

Note: includes both blocking and non-blocking code.
