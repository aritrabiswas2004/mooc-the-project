import os
import requests
import time
from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

start = time.time()
first_req = True
dirname = os.path.dirname(__file__)

@app.route('/todos', methods=['POST'])
def handle_todos():
    response = requests.post(os.environ.get('TODO-SVC-LINK'), data=request.form)
    if response.status_code == 200:
        return redirect("/")
    else:
        return "Something went wrong"

@app.route('/')
def main():
    global start
    global first_req

    last_refreshed = time.time()
    elapsed = abs(start - last_refreshed)

    if elapsed > 600 or first_req:
        first_req = False
        response = requests.get(os.environ.get('RANDOM-PIC-URL'))

        if response.status_code == 200:
            # change when deploying in k8s
            with open(os.path.join(dirname, "static/image.jpg"), "wb") as fileptr:
                fileptr.write(response.content)

        start = last_refreshed

    response_todos = requests.get(os.environ.get('TODO-SVC-LINK')).json()

    return render_template("index.html", todos=response_todos)

if __name__ == '__main__':
    app.run("0.0.0.0", port=int(os.environ.get("APP-PORT", 8080))) # leaving 8080 just as backup just in case
