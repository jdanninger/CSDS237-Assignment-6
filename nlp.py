import streamlit as st
# NLP Pkgs
from textblob import TextBlob
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
import re

nltk.download('wordnet')
nltk.download('omw-1.4')

st.title('Jakob\'s Sentiment Analysis Web App')
st.subheader('Created By Jakob Danninger for Prof Jayapandian\'s CSDS237')


u_input = st.text_area("Add text for sentiment analysis", "")


if st.button("Submit"):
    def clean_text(text):
        text = re.sub(r"[^A-Za-z0-9]", " ", text)
        text = re.sub(r"\'s", " ", text)
        text = re.sub(r"http\S+", " link ", text)
        text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)
        text = text.split()
        lemmatizer = WordNetLemmatizer()
        lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
        text = " ".join(lemmatized_words)
        return text
    cleaned_text = clean_text(u_input)


    # Sentiment Analysis
    blob = TextBlob(cleaned_text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        custom_emoji = ':blush:'
        st.success('Happy '  + custom_emoji)
    elif polarity < 0:
        custom_emoji = ':disappointed:'
        st.error('Sad ' + custom_emoji)
    else:
        custom_emoji = ':confused:'
        st.warning('Neutral ' + custom_emoji)
    st.success("Polarity score is: " + str(polarity))



