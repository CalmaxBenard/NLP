# Import packages
import nltk
import streamlit as st
from textblob import TextBlob
from nltk.stem.wordnet import WordNetLemmatizer
import re

nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


def main():
    # page configuration
    st.set_page_config(page_title="NLP App", page_icon=":robot_face:")

    # user input
    st.title("NLP")
    st.subheader("Welcome to our Application")
    text = st.text_area("Enter Your Text")

    # cleaning the text
    # keeping only text and digits
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    # remove whitespace
    text = re.sub(r"\'s", " ", text)
    # removing links if any
    text = re.sub(r"http\S+", " link ", text)
    # removes punctuations and numbers
    text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)
    # splitting text
    text = text.split()
    # Lemmatizer
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
    text = " ".join(lemmatized_words)

    # Predictions
    if st.button("Analyze"):
        blob = TextBlob(text)
        result = blob.sentiment.polarity
        if result > 0.0:
            emoji = ":blush:"
            st.success("Happy: {}".format(emoji))
        elif result < 0.0:
            emoji = ":disappointed:"
            st.warning("Sad: {}".format(emoji))
        else:
            emoji = ":confused:"
            st.info("Confused: {}".format(emoji))
        st.success("Polarity Score is: {}".format(result))


if __name__ == "__main__":
    main()
