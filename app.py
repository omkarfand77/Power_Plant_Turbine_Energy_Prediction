import pickle
import time
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
st.title('GAS-STEAM TURBINE ENERGY PREDICTION')
with st.sidebar:
    st.write('''A combined-cycle power plant comprises gas turbines, steam turbines, and heat recovery 
            steam generators. In this type of plant, the electricity is generated by gas and steam turbines 
            combined in one cycle. Then, it is transferred from one turbine to another. We have to model the 
            energy generated as a function of exhaust vacuum and ambient variables and use that model to 
            improve the plant's performance.''')

# Load the model
with open('model.pkl', 'rb') as load:
    model = pickle.load(load)

# Imputer (you need to define this based on how you handled missing values during model training)
# Example: imputer = SomeImputer()
# Replace 'SomeImputer()' with the actual imputer you used during training.


def predict(temperature, exhaust_vacuum, amb_pressure, r_humidity):
    # Make prediction
    scaler=StandardScaler()
    input_data = scaler.fit_transform([[temperature, exhaust_vacuum, amb_pressure, r_humidity]])
    prediction = model.predict(input_data)
    return prediction


def main():
    # Input fields
    temperature = st.number_input('temperature: ')
    exhaust_vacuum = st.number_input('exhaust_vacuum: ')
    amb_pressure = st.number_input('amb_pressure: ')
    r_humidity = st.number_input('r_humidity: ')

    # Button Logic
    if st.button('Predict'):
        # Call the prediction function
        result = predict(temperature, exhaust_vacuum, amb_pressure, r_humidity)
        st.success(f'Energy Production: {result}')

if __name__ == '__main__':
    main()