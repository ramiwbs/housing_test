import pickle
import streamlit as st
import pandas as pd

# NEED TO BE CHANGED TO WHERE YOUR PATH IS
model = pickle.load(open('/Users/ramialsalman/Desktop/deploy_model/models/trained_pipe_lr.sav', 'rb'))
 

LotArea = st.number_input("Lot Area")
TotalBsmtSF = st.number_input("Basement Square Feet")
BedroomAbvGr = st.number_input("Number of Bedrooms")
GarageCars = st.number_input("Car spaces in Garage")
 
import pandas as pd
new_house = pd.DataFrame({
    'LotArea':[LotArea],
    'TotalBsmtSF':[TotalBsmtSF], 
    'BedroomAbvGr':[BedroomAbvGr], 
    'GarageCars':[GarageCars]
})
 
prediction = model.predict(new_house)
 
st.write("The price of the house is:", prediction)