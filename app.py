from flask import Flask
from waitress import serve
import threading
import time
import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    # Every time this method is called, a background task is started.
    thread = threading.Thread(target=background_task, args=())
    thread.daemon = False;
    thread.start()
    return "Hello World!"


def background_task():
    # Below code is just for fun.
    # The purpose here is to run a long running shell operation.
    time.sleep(5)
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    return


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=80)
