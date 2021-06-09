from flask import Flask
from flask import request
from logging.config import dictConfig


dictConfig({
    'version': 1,
    'formatters':
    {
        'default': {
            'format': '[%(asctime)s] %(levelname)s: %(message)s',
        }
    },
    'handlers':
    {
        'wsgi':
        {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'app.log',
            'maxBytes': 1024,
            'backupCount': 3,
            'formatter': 'default'
        }
    },
    'root':
    {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__)


@app.before_request
def log_request_info():
    app.logger.debug(f'[{request.path}] endpoint was reached')


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/status")
def status():
    return {"data": {"UserCount": 140, "UserCountActive": 23}}


@app.route("/metrics")
def metrics():
    return {"result": "OK - healthy"}


if __name__ == "__main__":
    app.run(host='0.0.0.0')
