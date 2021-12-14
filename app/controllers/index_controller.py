"""controller for index page"""
from flask import render_template
from app.controllers.controller import ControllerBase


class IndexController(ControllerBase):
    """index controller"""
    @staticmethod
    def get():
        """index page controller"""
        return render_template('index.html')
