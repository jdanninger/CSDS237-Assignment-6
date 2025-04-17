import streamlit as st
# NLP Pkgs
from textblob import TextBlob
from nltk.stem.wordnet import WordNetLemmatizer
import re

st.title('Jakob\'s Sentiment Analysis Web App')
st.subheader('Created By Jakob Danninger for Prof Jayapandian\'s CSDS237')


u_input = st.text_area("Add text for sentiment analysis", "")


if st.button("Submit"):
    def clean_text(text):
        # clean stuff here with regex??
        return text

    cleaned_text = clean_text(u_input)
    st.write(cleaned_text)