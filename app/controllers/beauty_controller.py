from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash, app

# from data.create_data import DataCreator


class BeautyController(ControllerBase):

    @staticmethod
    def get():
        app.logger.info('Processing default request')
        # my_Data = getattr(DataCreator, 'create_data')
        # data_bt = DataFaker.create_fake_users(20)
        # my_Data = list(data_bt.values)
        return render_template('beauty.html') #, my_Data=my_Data)
