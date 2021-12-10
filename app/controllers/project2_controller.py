from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash

from dto.printing_results import Print


class OOPsController(ControllerBase):
    @staticmethod
    def get():
        page = request.args.get('page')
        if page == "pylint":
            return render_template('pylintfile.html')
        elif page == "caloop":
            return render_template('caloops.html')
        elif page == "aaa-test":
            return render_template('aaatesting.html')
        else:
            return render_template('solid.html')

        return render_template('solid.html')

