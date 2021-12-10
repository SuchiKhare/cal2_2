from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash

from data.printing_results import Print


class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form['input1'] == '' or request.form['input2'] == '':
            error = 'Please enter a numerical values for input 1 and or input 2'
        else:
            flash('Congratulations !! Calculations are successful')

            # get the values out of the form
            input1 = request.form['input1']
            input2 = request.form['input2']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (input1, input2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            my_output = str(Calculator.get_last_result_value())
            print_lst = [Print(input1, input2, operation, my_output), Print(1, 1, "Multiplication", 2),
                         Print(input1, input2, operation, my_output), Print(1, 1, "Multiplication", 2),
                         Print(input1, input2, operation, my_output), Print(1, 1, "Multiplication", 2),
                         Print(input1, input2, operation, my_output), Print(1, 1, "Multiplication", 2),
                         Print(input1, input2, operation, my_output), Print(1, 1, "Multiplication", 2),
                         Print(input1, input2, operation, my_output), Print(1, 1, "Multiplication", 2),
                         Print(input1, input2, operation, my_output), Print(1, 1, "Multiplication", 2),
                         Print(input1, input2, operation, my_output), Print(1, 1, "Multiplication", 2),
                         Print(input1, input2, operation, my_output), Print(1, 1, "Multiplication", 2),
                         Print(input1, input2, operation, my_output), Print(1, 1, "Multiplication", 2),
                         Print(input1, input2, operation, my_output), Print(1, 1, "Multiplication", 2),
                         Print(input1, input2, operation, my_output), Print(1, 1, "Multiplication", 2),
                         Print(input1, input2, operation, my_output), Print(1, 1, "Multiplication", 2),
                         Print(input1, input2, operation, my_output), Print(1, 1, "Multiplication", 2)]
            return render_template('result.html', input1=input1, input2=input2, operation=operation \
                                   , result=my_output, print_lst=print_lst)
        return render_template('calculator.html', error=error)

    @staticmethod
    def get():
        return render_template('calculator.html')
