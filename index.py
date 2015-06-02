from flask import render_template
from models import User, app
import requests
import json

@app.route("/welcome/<my_name>")
def hello_with_name(my_name):
    return "Welcome " + my_name

@app.route("/martha")
def martha():
    return "hello martha"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/query')
def query():
    r = requests.get("http://www.omdbapi.com/?t=Frozen&y=&plot=short&r=json")
    results = json.loads(r.text)
    return render_template('query.html', results=results)

@app.route('/listusers')
def list_users():
    user_list = User.query.all()
    return render_template('users.html', user_list=user_list)

if __name__ == "__main__":
    app.run(debug=True)
