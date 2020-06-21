from flask import Flask
from waitress import serve
import threading
import datetime
import subprocess

app = Flask(__name__)


@app.route("/thread")
def thread():
    t = threading.Thread(target=subprocess_background_thread, args=())
    t.name = "my thread name"
    t.daemon = False
    t.start()
    return "Thread created\n"


@app.route("/thread_count")
def thread_count():
    active_count = threading.active_count()
    return f'active thread count: {active_count}\n'


def subprocess_background_thread():
    subprocess.run(["sleep", "5"])
    print("THREAD EXECUTED : " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    return


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
