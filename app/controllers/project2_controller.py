from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash


class OOPsController(ControllerBase):
    @staticmethod
    def get():
        page = request.args.get('page')
        if page == "pylint":
            return render_template('pylint.html')
        elif page == "cal-oop":
            return render_template('oops.html')
        elif page == "aaa-test":
            return render_template('aaa.html')
        else:
            return render_template('solid.html')
