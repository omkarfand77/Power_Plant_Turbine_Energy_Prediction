import pickle
import time
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
st.title('_*:red[GAS-STEAM TURBINE ENERGY PREDICTION]*_')
with st.container():
    with st.sidebar:
        st.header('_*:red[GAS-STEAM TURBINE ENERGY PREDICTION]*_',  divider='rainbow')
        st.write('**MR. OMKAR SUNILDATT FAND**')
        st.page_link("https://www.linkedin.com/in/omkar-s-fand-043755149", label=":blue[LinkedIn]")
        st.page_link("http://www.gmail.com/", label=":blue[E-mail: omkarfand77@gmail.com]")
        st.subheader('Objective', divider='rainbow')
        st.write('''A combined-cycle power plant comprises gas turbines, steam turbines, and heat recovery 
            steam generators. In this type of plant, the electricity is generated by gas and steam turbines 
            combined in one cycle. Then, it is transferred from one turbine to another. We have to model the 
            energy generated as a function of exhaust vacuum and ambient variables and use that model to 
            improve the plant's performance.''')
        st.subheader('Steps Involved', divider='rainbow')
        st.write('''

    1. **Power Plant Configuration:** Integrated gas turbines, steam turbines, and heat recovery steam generators to generate electricity.
    2. **Energy Transfer:** Modeled electricity generation through a tandem gas and steam turbine cycle, enabling the transfer of energy between turbines.
    3. **Feature Engineering and Dimensionality Reduction:** Applied dimensionality reduction techniques to optimize the feature set for better model performance.
    4. **Model Building:** Constructed a Random Forest Regression model to predict energy output based on exhaust vacuum and ambient variables.
    5. **Model Evaluation:**  Evaluated the model using cost functions to ensure its effectiveness in optimizing plant performance.
    6. **Deployment:** Deploy the model using the Streamlit framework for real-time application.''')
        st.subheader('Tools & Librares Used', divider='rainbow')
        st.write('Python, Pandas, Numpy, Scikit-Learn, Malplotlib, Seaborn, Streamlit')



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
        st.success(f'Energy Production: {result}MW')

if __name__ == '__main__':
    main()