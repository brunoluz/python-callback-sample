from flask import Flask
from waitress import serve
import threading
import datetime
import subprocess
import asyncio

app = Flask(__name__)


@app.route("/thread")
def hello():
    # Every time this method is called, a background task is started.
    thread = threading.Thread(target=subprocess_background_thread, args=())
    thread.daemon = False
    thread.start()
    return "Thread created\n"


def subprocess_background_thread():
    # TODO: Use asyncio to work with subprocess: https://docs.python.org/pt-br/3.7/library/asyncio-subprocess.html
    subprocess.run(["sleep", "5"])
    print("THREAD EXECUTED : " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    return


@app.route("/task")
def task():
    # TODO: This method is not running asynchronously.
    # Need to investigate further.
    asyncio.run(subprocess_background_task())
    return "Task scheduled\n"


async def subprocess_background_task():
    subprocess.run(["sleep", "5"])
    print("TASK EXECUTED : " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    return


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
