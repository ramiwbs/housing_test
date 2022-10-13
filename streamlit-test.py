import pickle
import streamlit as st
import pandas as pd

# NEED TO BE CHANGED TO WHERE YOUR PATH IS
model = pickle.load(open('models/trained_pipe_lr.sav', 'rb'))
 

new_house = pd.DataFrame({
    'LotArea':[9000],
    'TotalBsmtSF':[1000], 
    'BedroomAbvGr':[5], 
    'GarageCars':[4]
})
 
prediction = model.predict(new_house)
 
st.write("The price of the house is:", prediction)

