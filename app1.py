#```python
from flask import Flask, request, render_template
import sklearn
import numpy as np
import joblib

# Load model
obj = joblib.load('california.joblib')

model = obj['model']
columns = obj['columns']

print(columns)

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html', columns=columns)


@app.route('/predict', methods=['POST'])
def predict():

    input_data = []

    for i in columns:
        val = request.form.get(i)
        input_data.append(float(val))

    prediction = model.predict([input_data])

    return render_template(
        'index.html',
        columns=columns,
        prediction=round(float(prediction[0]), 4)
    )


if __name__ == '__main__':
    app.run(debug=True)
