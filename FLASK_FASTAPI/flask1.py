from flask import Flask

app = Flask(__name__)

@app.route('/')
def display() :
    return "<h1> Hello JLL </h1>"


if __name__ == "__main__" :
    app.run()