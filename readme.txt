ChatGPT
================================
Hi Your role is good UI developer
I have developed a flask application i want to add UI layer on that for frontend
add HTML CSS style make a clear UI

I also provided my app code
=======================================
from flask import Flask ,request
import sklearn
import numpy as np
import joblib


obj = joblib.load('california.joblib')
model=obj['model']
columns =obj['columns']
print(columns)

app=Flask(__name__)
@app.route('/')
def main():
    return('welcome')

@app.route('/predict')
def predict():
    input=[]
    for i in columns:
        val = request.args.get(i)
        input.append(float(val))

    prediction = model.predict([input])
    return str(prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
=====================================
steps to activate venv
========================

C:\Users\creat\Documents\Naresh it\flask_example\FlaskProject>cd C:\Users\creat\Documents\Naresh it\Venv


python -m venv lr_proj ---->>>  for create venv 

C:\Users\creat\Documents\Naresh it\Venv>cd lr_proj

C:\Users\creat\Documents\Naresh it\Venv\lr_proj>cd Scripts

C:\Users\creat\Documents\Naresh it\Venv\lr_proj\Scripts>activate

(lr_proj) C:\Users\creat\Documents\Naresh it\Venv\lr_proj\Scripts>


                         Now>>>
                         =====

(lr_proj) C:\Users\creat\Documents\Naresh it\Venv\lr_proj\Scripts>cd C:\Users\creat\Documents\Naresh it\flask_example\FlaskProject


(lr_proj) C:\Users\creat\Documents\Naresh it\flask_example\FlaskProject>pip install -r requirements.txt

            trhn ::pip install pandas 



