import os
from flask import Flask
from flask import render_template
from flask import request

import task

app = Flask(__name__)

@app.route("/")
def hello():
    name = request.args.get('name', 'Jane doe')
    result = task.hello.delay(name)
    result.wait()
    return render_template('index.html', celery=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
