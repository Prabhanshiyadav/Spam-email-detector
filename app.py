import streamlit as st

st.title("Spam Email Detector")

email_text = st.text_area("Enter Email Text")

if st.button("Predict"):
    if email_text:
        st.success("This is a test. Your model will predict here!")
    else:
        st.warning("Please enter some text first.")
