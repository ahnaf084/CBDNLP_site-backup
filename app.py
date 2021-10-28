import pickle

import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

category = ['Geopolitical', 'Hate speech', 'Personal attack', 'Political', 'Profanity', 'Religious', 'Sexual harassment']


def predict(comm, catg):
    model = load_model(
        "CyberbullyingDetection.h5")
    # model.summary()

    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    sentence = [comm]
    sequences = tokenizer.texts_to_sequences(sentence)
    padded = pad_sequences(sequences, maxlen=1334, padding='post', truncating='post')
    prediction_main = model.predict(padded)

    i = 0
    for k in range(len(prediction_main[0])):
        print(category[i] + ' = %f %%' % (prediction_main[0, k] * 100))
        i = i + 1

    result = (np.where(prediction_main == max(prediction_main[0])))

    catg = result[1][0]

    return max(prediction_main[0]), catg


catgr = 0

st.title("Cyberbullying Detection using NLP")
comment = st.text_area("Enter a comment in Bangla text")

if st.button("Analyze"):
    with st.spinner("Analyzing the text …"):
        prediction = predict(comment, catgr)
        if prediction[0] > 0.8:
            st.success("This comment contains {:.2%} ".format(prediction[0]) + category[prediction[1]])
            # st.balloons()
        elif 0.6 < prediction[0] < 0.8:
            st.error("This might be a cyberbullying comment which contains {:.0%} ".format(prediction[0]) + category[
                prediction[1]])
        else:
            st.warning("This is not a cyberbullying comment")
