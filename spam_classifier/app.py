import streamlit as st
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

st.title("📧 Spam Email Classifier")

input_text = st.text_area("Enter your message:")

if st.button("Predict"):
    data = vectorizer.transform([input_text])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("This is SPAM ❌")
    else:
        st.success("This is NOT SPAM ✅")