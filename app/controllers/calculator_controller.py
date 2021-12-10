from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash

from dto.printing_results import Print


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
            # for this HW this is the Dummy Data .
            # In project 3 , this is dynamically populated from csv after calculations
            # This HW is just to show the use of beautiful tables in the frontend using javascript
            # and calling the javascript by  $('#data').DataTable() in result html
            # flow is app.py -->controller--> result.html
            # added 3 scripts in base.html
            # As it was not mentioned where the data to take from - using faker, from csv , dynamic calculation
            print_lst = [Print(input1, input2, operation, my_output),
                         Print(1, 1, "multiplication", 1.0),
                         Print(100, 10, "division", 10.0),
                         Print(1, 1, "division", 1.0),
                         Print(5, 5, "addition", 10.0),
                         Print(1, 1, "addition", 2.0),
                         Print(15, 5, "addition", 20.0),
                         Print(1, 1, "addition", 2.0),
                         Print(2, 1.1, "multiplication", 2.2),
                         Print(1.1, 1, "multiplication", 1.1),
                         Print(.01, 10, "multiplication", 0.1),
                         Print(10, 10, "subtraction", 0.0),
                         Print(10, 11, "subtraction", -1.0),
                         Print(101, 1, "subtraction", 100.0),
                         Print(10, 21, "subtraction", -11.0),
                         Print(2, 1, "multiplication", 2.0),
                         Print(1, 1, "multiplication", 1.0),
                         Print(1, 1, "multiplication", 1.0),
                         Print(1, 1, "multiplication", 1.0),
                         Print(1, 1, "multiplication", 1.0),
                         Print(50, 50, "division", 1.0),
                         Print(20, 100, "division", 0.2),
                         Print(0.5, 0.5, "multiplication", 0.25),
                         Print(1, 1, "subtraction", 0.0),
                         Print(10, 1, "subtraction", 9.0)]
            return render_template('result.html', input1=input1, input2=input2, operation=operation \
                                   , result=my_output, print_lst=print_lst)
        return render_template('calculator.html', error=error)

