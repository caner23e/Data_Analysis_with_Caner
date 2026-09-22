import streamlit as st 

st.title("Hello this is my first so called app")
st.write("I will play around with the button and checkbox functions")
st.write("Are you ready?")
button1= st.button("I am ready")
if button1:
    st.write("oke lets get started")
st.write("Do you have programming experiences?")
like1 = st.checkbox("Yes I do have programming experiences")
like2 = st.checkbox("Programming what?")

if like1: 
    st.write("how long have you been programming?")
    answer1 = st.checkbox("For more than a year")
    answer2= st.checkbox("For less than a year")
    if answer1:
        st.text("Go and touch some grass")
    if answer2:
        st.text("Noob")
if like2:
    st.write("Have you been living on the moon??")