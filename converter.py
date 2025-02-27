#unit converter 

import streamlit as st

st.header("UNIT CONVERTER")

#choose Unit type

conversionType = st.selectbox(label='Choose Unit Type:', options=["Length", "Temperature", "Area", "Weight", "Time"])

#Select Unit 

if conversionType == "Length" :
    fromUnit = st.selectbox(label='From', options=["Meter", "Inch", "Centimeter", "Kilometer", "Milimeter", "Micrometer", "Nanometer", "Mile", "Yard", "Foot"])
elif conversionType == "Temperature":
    fromUnit = st.selectbox(label='From', options=["celsius", "kelvin", "Fahrenheit"])
elif conversionType == "Area":
    fromUnit = st.selectbox(label='From', options=["Square Meter", "Square Kilometer", "Square Centimeter", "Square Milimeter", "Square Micrometer", "Hectare", "Square Mile", "Square Yard", "Square Foot", "Square Inch", "Arce"])




# here we type value
value = st.number_input(label='from' , min_value = 0, max_value = 999999999)



#To Unit


if conversionType == "Length" :
    ToUnit = st.selectbox(label='From', options=["Meter", "Inch", "Centimeter", "Kilometer", "Milimeter", "Micrometer", "Nanometer", "Mile", "Yard", "Foot"])
elif conversionType == "Temperature":
    ToUnit = st.selectbox(label='From', options=["celsius", "kelvin", "Fahrenheit"])
elif conversionType == "Area":
    ToUnit = st.selectbox(label='From', options=["Square Meter", "Square Kilometer", "Square Centimeter", "Square Milimeter", "Square Micrometer", "Hectare", "Square Mile", "Square Yard", "Square Foot", "Square Inch", "Arce"])


if fromUnit == "Meter" == ToUnit =="Centimeter" :
    resultValue = value * 100








    



