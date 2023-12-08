
from flask import Flask 

app = Flask(__name__)


@app.route('/ack/<name>')
def acknowledge(name) :
    return 'Thanks for using Flask Service API : %s' % name


if __name__ == "__main__" :
    app.run("localhost", 8080)