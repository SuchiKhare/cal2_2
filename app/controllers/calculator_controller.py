"""calculator controller class"""
from flask import render_template, request
from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from calc.utils.utility import Utility


class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form['input1'] == '' or request.form['input2'] == '':
            error = 'Please enter a numerical values for input 1 and or input 2'
        else:
            # get the values out of the form
            input1 = request.form['input1']
            input2 = request.form['input2']
            operation = request.form['operation']
            my_tuple = (input1, input2)
            # this will call the correct operation
            data = {
                'result': '',
                'input1': [input1],
                'input2': [input2],
                'operation_name': [operation]
            }

            Calculator.write_history_to_csv(data)
            full_history_df = Calculator.get_history_from_csv()
            print_lst = Utility.convert_df_dto(full_history_df)
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
            return render_template('result.html', input1=input1, input2=input2, operation=operation, result=result,
                                   print_lst=print_lst)
        return render_template('calculator.html', error=error)

    @staticmethod
    def get():
        return render_template('calculator.html')
