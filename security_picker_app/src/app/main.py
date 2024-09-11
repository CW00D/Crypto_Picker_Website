import json
from flask import Flask, make_response
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import send_from_directory
from flask import url_for
from flask import send_file
import logging
from flask_cors import CORS, cross_origin
import json


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.INFO)
cors = CORS(app, resources={r"/institutions": {"origins": "*"}, r"/institutionConfigurations": {
            "origins": "*"}, r"/licenses": {"origins": "*"}, r"/license": {"origins": "*"}, r"/institutionConfiguration": {"origins": "*"}, r"/license": {"origins": "*"},
    r"/generateYaml": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/", methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        try:
            username = request.form["username"]
            password = request.form["password"]
            session['logged_in'] = 1
            if username == "ECAdmin" and password == "EyesclearPwd123@":
                return redirect(url_for('index'))
            else:
                error = 'Invalid Username/Password'
        except:
            error = "Server error!"
    return render_template('login.html', error=error)