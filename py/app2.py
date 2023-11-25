from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!22</p>"
@app.route("/aa")
def hello_world2():
    return "<p>33333</p>"
@app.route("/aaa")
def hello_world3():
    return render_template('qa.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)