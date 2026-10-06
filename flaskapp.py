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
