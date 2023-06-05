import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import streamlit as st
import joblib

model= open("C:/Users/Dell/Desktop/BA project/linear_Regression.pkl", "rb")
predictor=joblib.load(model)

st.title("CASH PREDICTION IN ATM")

st.sidebar.title("Features")
parameter_list=["No Of Withdrawals","Weekday Id","Festival Religion Id","Working Day Id","Holiday Sequence Id"]
parameter_input_values=[]
parameter_default_values=[67,0,4,0,1]
values=[]

values= st.sidebar.slider(label="No Of Withdrawals", key="No Of Withdrawals",value=98, min_value=1, max_value=188, step=1)
parameter_input_values.append(values)
       
data_dim = st.sidebar.radio('Select Day',('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'))
if data_dim=='Sunday':
    parameter_input_values.append(0)
elif data_dim=='Monday':
    parameter_input_values.append(1)
elif data_dim=='Tuesday':
    parameter_input_values.append(2)
elif data_dim=='Wednesday':
    parameter_input_values.append(3)
elif data_dim=='Thursday':
    parameter_input_values.append(4)
elif data_dim=='Friday':
    parameter_input_values.append(5)
elif data_dim=='Saturday':
    parameter_input_values.append(6)

data_dim = st.sidebar.radio('Select Festival Religion',('Christian','Hindu','Muslim','National Festival','None'))
if data_dim=='Christian':
    parameter_input_values.append(0)
elif data_dim=='Hindu':
    parameter_input_values.append(1)
elif data_dim=='Muslim':
    parameter_input_values.append(2)
elif data_dim=='National Festival':
    parameter_input_values.append(3)
elif data_dim=='None':
    parameter_input_values.append(4)


data_dim = st.sidebar.radio('Working Day or Not',('Working day','Holiday'))
if data_dim=='Working day':
    parameter_input_values.append(1)
elif data_dim=='Holiday':
    parameter_input_values.append(0)


data_dim = st.sidebar.radio('Select Sequence\nW-Working day\nH-Holiday',('HHH','HHW','HWH','HWW','WHH','WHW','WWH','WWW'))
if data_dim=='HHH':
    parameter_input_values.append(0)
elif data_dim=='HHW':
    parameter_input_values.append(1)
elif data_dim=='HWH':
    parameter_input_values.append(2)
elif data_dim=='HWW':
    parameter_input_values.append(3)
elif data_dim=='WHH':
    parameter_input_values.append(4)
elif data_dim=='WHW':
    parameter_input_values.append(5)
elif data_dim=='WWH':
    parameter_input_values.append(6)
else:
    parameter_input_values.append(7)


st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: rgb(0, 255, 255);
        
    .big-font {
        font-size:35px !important;
    }
    </style>
    """, unsafe_allow_html=True)

if st.button("Click Here to Predict"):
    prediction = int(predictor.predict([parameter_input_values])[0])
    x="<h3 class='big-font'>"+str(prediction)+"</h3>"
    st.markdown(x,unsafe_allow_html=True)


