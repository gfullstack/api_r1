#!/bin/python
# -*- coding: utf-8 -*-
# from flask import Flask,render_template

# DEBUG = True
# app = Flask(__name__)
 
# @app.route('/')
# def index():
	# return 'App Flask - It is Working...'
	#return render_template('index.html') 
# if __name__ == '__main__':
        # app.run()


import os
from app import create_app

app = create_app()

if __name__ == '__main__':
	app.run()