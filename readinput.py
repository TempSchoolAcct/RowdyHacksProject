from flask import Flask, render_template, redirect, url_for,request
from flask import make_response
app = Flask(fullxtest)

@app.route("/")
def home():
    return "hi"
@app.route("/index")

@app.route('/login', methods=['GET', 'POST'])
def login():
   message = None
   if request.method == 'POST':
        datafromjs = request.form['mydata']
        result = "return this"
        resp = make_response('{"response": '+result+'}')
        resp.headers['Content-Type'] = "application/json"
        return resp
        return render_template('login.html', message='')

if __name__ == "__main__":
    app.run(debug = True)
   
# (fullXtest) readinput.py - python code to read input <hostname> from javascript web app and pass to fullXtest.py
# by 404TeamNotFound
