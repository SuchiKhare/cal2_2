"""OOP controller for project2"""

from flask import render_template, request

from app.controllers.controller import ControllerBase  # pylint: disable=import-error


class OOPsController(ControllerBase):
    """OOPS controller"""

    @staticmethod
    def get():
        """get different pages from project2"""
        page = request.args.get('page')
        name = ""
        if page == "pylint":
            name = 'pylint.html'
        elif page == "cal-oop":
            name = 'oops.html'
        elif page == "aaa-test":
            name = 'aaa.html'
        else:
            name = 'solid.html'
        return render_template(name)
