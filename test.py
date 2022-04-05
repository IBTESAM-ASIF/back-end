from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/about")
def about():
    return "<h1>About</h1>"

if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()