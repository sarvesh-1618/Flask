from flask import Flask
app = Flask(__name__)  # app instance
@app.route('/')
def greet():
    return('welcome')


@app.route('/greet1')
def greet1():
    return('Good morning')


if __name__=='__main__':
    app.run(debug = True)

