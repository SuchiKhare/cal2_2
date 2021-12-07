from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash


class BeautyController(ControllerBase):

    @staticmethod
    def get():
        return render_template('beauty.html')
