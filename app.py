import streamlit as st
import pickle
import numpy as np

# Load the model from the file
pickle_filename = './notebooks/xgboost_model.pkl'
with open(pickle_filename, 'rb') as file:
    model = pickle.load(file)

# Function to predict energy output
def predict_energy_output(ambient_temp, exhaust_vacuum, ambient_pressure, relative_humidity):
    # Create a numpy array with the input values
    input_data = np.array([[ambient_temp, exhaust_vacuum, ambient_pressure, relative_humidity]])
    # Predict the energy output using the loaded model
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit app
st.title('Energy Output Prediction for Thermal Power Plant')

# Input fields
ambient_temp = st.number_input('Ambient Temperature (°C)', min_value=-50.0, max_value=50.0, step=0.1)
exhaust_vacuum = st.number_input('Exhaust Vacuum (cm Hg)', min_value=0.0, max_value=100.0, step=0.1)
ambient_pressure = st.number_input('Ambient Pressure (milibar)', min_value=500.0, max_value=1100.0, step=0.1)
relative_humidity = st.number_input('Relative Humidity (%)', min_value=0.0, max_value=100.0, step=0.1)

if st.button('Predict'):
    # Call the prediction function
    energy_output = predict_energy_output(ambient_temp, exhaust_vacuum, ambient_pressure, relative_humidity)
    st.success(f'Predicted Net Hourly Electrical Energy Output: {energy_output:.2f} MW')
