from flask import Flask
app = Flask(__name__)  # app instance
@app.route('/')
def greet():
    return('welcome')


@app.route('/greet1') #main page
def greet1():
    return('Good morning')


if __name__=='__main__':
    app.run(host = '0.0.0.0' , port ='8000' , debug = True)

