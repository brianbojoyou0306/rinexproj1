import streamlit as st
import joblib
model = joblib.load('gender (1)')
import numpy as np 
st.title('GENDER CLASSIFIER')
ip1 = st.number_input('Enter the height')
ip2 = st.number_input('enter the weight')
ls=np.append(ip1,ip2)
op = model.predict([ls])
if st.button('predict'):
  st.title(op[0])
