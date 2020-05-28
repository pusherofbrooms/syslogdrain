from __future__ import print_function
from flask import Flask
from flask import request
import os
import sys


app = Flask(__name__)

port = int(os.getenv("PORT", 9099))

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    print(request.data, file=sys.stdout)
    return ""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
