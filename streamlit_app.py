import joblib
import pandas as pd 
import numpy as np 
import sklearn
import streamlit as st



obj =  joblib.load('california.joblib')
Model=obj['model']
columns = obj['columns']


INPUT= []
for i in columns:
    val = st.number_input(f'Enter {i}')
    INPUT.append(val)  #1D

if st.button('Predict'):
    out=Model.predict([INPUT])
    st.success(f'the med house value is :{out}')