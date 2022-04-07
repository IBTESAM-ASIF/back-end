from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/connect")
def about():
    return "<h1>connect</h1>"

@app.route("/results")
def about():
    return "<h1>results</h1>"

if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()