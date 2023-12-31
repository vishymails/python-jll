
from flask import Flask 

app = Flask(__name__)


@app.route('/ack/<int:age>')
def displayAge(age) :
    return 'Thanks for using Flask Service API : %d' % age



@app.route('/takefloat/<float:salary>')
def salary(salary) :
    return 'Display Salary API : %f' % salary



if __name__ == "__main__" :
    app.run("localhost", 8080)