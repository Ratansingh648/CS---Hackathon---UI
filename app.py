# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:47:29 2020

@author: Ratan Singh
"""

from flask import Flask, render_template, request, redirect
import os
from werkzeug.utils import secure_filename
import pandas as pd

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = "static/uploads"


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/load-testing")
def linkedIssuers():
    return render_template("loadTesting.html")


@app.route('/analytics')
def externalRating():
    return render_template('analytics.html')



@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        files = ['marketbond', 'loan', 'fx', 'fospread', 'proxy']
        for fileName in files:
            try:
                f = request.files[fileName]
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            except:
                pass
    return redirect('/custom-run')


if __name__ == "__main__":
    app.run(debug=True)
