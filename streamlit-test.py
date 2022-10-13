import pickle
import streamlit as st
import pandas as pd

# NEED TO BE CHANGED TO WHERE YOUR PATH IS
model = pickle.load(open('/app/deplymodel_app/models/trained_pipe_lr.sav', 'rb'))

st.title('Welcome to the House Prediction app')

st.subheader('Enter the information of the house')

LotArea = st.slider('Lot Area', 0, 1000, 0) 
TotalBsmtSF = st.slider('Basement Square Feet', 0, 1000, 0)
BedroomAbvGr = st.slider('Number of Bedrooms', 0, 10, 0)
GarageCars = st.slider('Car spaces in Garage', 0, 10, 0)


import pandas as pd
new_house = pd.DataFrame({
    'LotArea':[LotArea],
    'TotalBsmtSF':[TotalBsmtSF], 
    'BedroomAbvGr':[BedroomAbvGr], 
    'GarageCars':[GarageCars]
})
 
prediction = model.predict(new_house)
 
st.write("The price of the house is:", prediction)
