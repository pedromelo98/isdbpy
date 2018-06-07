from flask import Flask

app = Flask(__name__, template_folder='../templates', static_folder='../static')

import control.home

app.run(debug=True)
