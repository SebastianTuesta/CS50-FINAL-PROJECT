# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 13:27:29 2018

@author: Sebastian
"""

from flask import Flask, render_template, request, jsonify
from web_scrap import Web_scrap

import json


app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
	if request.method == 'POST':
		analize = request.form["analize"]
		length = int(request.form["length"])
		
		data = Web_scrap(analize, length)
		

		if len(data['nodes'])>1:
			return render_template("web_scrap.html",data = data)
		else:
			return  render_template("index.html", warming = True)
	else:
		return render_template("index.html", warming = False)


if __name__ == "__main__":
    app.run()
    