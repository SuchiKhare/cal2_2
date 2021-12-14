""" History Controller"""
from flask import render_template, request, flash
from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from calc.history.calculations_csv import CalculationsCSV


class HistoryController(ControllerBase):
    """HistoryController for calculations"""
    @staticmethod
    def get():
        """get method for history"""
        page = request.args.get('act')
        if page == "clear":
            is_clear = Calculator.clear()
            if is_clear:
                flash('Cleared History!!')
            return render_template('calculator.html')
        else:
            count = CalculationsCSV.count_history()
            if count == 0:
                error = 'No history details available, Please perform calculations first to make history'
                return render_template('calculator.html', error=error)
            else:
                first_operation = CalculationsCSV.get_first_calculation_object()
                first_result = CalculationsCSV.get_first_calculation_result_value()
                last_operation = CalculationsCSV.get_last_calculation_object()
                last_result = CalculationsCSV.get_last_calculation_result_value()
                return render_template('history_details.html', count=count, first_operation=first_operation,
                                       first_result=first_result, last_operation=last_operation,
                                       last_result=last_result)
