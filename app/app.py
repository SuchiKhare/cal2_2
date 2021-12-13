"""A simple flask web app"""
from flask import Flask
from werkzeug.debug import DebuggedApplication

from app.controllers.history_controller import HistoryController
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.project2_controller import OOPsController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)


@app.route("/", methods=['GET'])
def index_get():
    """index"""
    return IndexController.get()


@app.route("/calculator", methods=['GET'])
def calculator_get():
    """calculator get"""
    return CalculatorController.get()


@app.route("/calculator", methods=['POST'])
def calculator_post():
    """calculator post"""
    return CalculatorController.post()


@app.route("/history", methods=['GET'])
def history_clear_get():
    """history clear"""
    return HistoryController.get()


@app.route("/project2", methods=['GET'])
def project2_get():
    """links for project2 for previous page"""
    return OOPsController.get()
