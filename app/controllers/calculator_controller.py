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
            # Dummy Data - in project 3 , this is dynamically populated from csv.
            # This HW is just to show the use of beautiful tables in the frontend
            print_lst = [Print(input1, input2, operation, my_output),
                         Print(1, 1, "Multiplication", 1),
                         Print(100, 10, "Division", 10.0),
                         Print(1, 1, "Division", 1),
                         Print(5, 5, "Addition", 10.0),
                         Print(1, 1, "Addition", 2.0),
                         Print(15, 5, "Addition", 20.0),
                         Print(1, 1, "Addition", 2.0),
                         Print(2, 1.1, "Multiplication", 2.2),
                         Print(1.1, 1, "Multiplication", 1.1),
                         Print(1, 10, "Multiplication", 0.1),
                         Print(10, 10, "Subtraction", 0.0),
                         Print(10, 11, "Subtraction", -1.0),
                         Print(101, 1, "Subtraction", 100.0),
                         Print(10, 21, "Subtraction", -11.0),
                         Print(2, 1, "Multiplication", 2),
                         Print(1, 1, "Multiplication", 1),
                         Print(1, 1, "Multiplication", 1),
                         Print(1, 1, "Multiplication", 1),
                         Print(1, 1, "Multiplication", 1),
                         Print(50, 50, "Division", 1.0),
                         Print(20, 100, "Division", 0.2),
                         Print(0.5, 0.5, "Multiplication", 0.25),
                         Print(1, 1, "Subtraction", 0.0),
                         Print(10, 1, "Subtraction", 9.0),]
            return render_template('result.html', input1=input1, input2=input2, operation=operation \
                                   , result=my_output, print_lst=print_lst)
        return render_template('calculator.html', error=error)

    @staticmethod
    def get():
        return render_template('calculator.html')
