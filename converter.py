#unit converter 

import streamlit as st

st.header("UNIT CONVERTER")

#choose Unit type

conversionType = st.selectbox(label='Choose Unit Type:', options=["Length", "Temperature", "Area", "Weight", "Time"])

if conversionType == "length" :
    selectUnit = st.selectbox(label='select Unit', options=["Meter", "Inch", "Centimeter"])
elif conversionType == "Temperature":
    selectUnit = st.selectbox(label='Select Unit', options=["celsius", "kelvin", "Fahrenheit"])

