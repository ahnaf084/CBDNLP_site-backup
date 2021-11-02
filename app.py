import ktrain
import streamlit as st

category = ['Geopolitical', 'Hate speech', 'Personal attack', 'Political', 'Profanity', 'Religious',
            'Sexual harassment']


def predict(comm, catg):
    model = ktrain.load_predictor('CyberbullyingDetection_kt')

    cat = model.predict(comm)
    probas = model.predict_proba(comm)

    return cat, round(max(probas) * 100, 2)


percentage = 0

st.title("Cyberbullying Detection")
comment = st.text_area("Enter text in Bangla")

if st.button("Detect"):
    with st.spinner("Analyzing the text …"):
        prediction = predict(comment, percentage)
        if prediction[1] > 80:
            st.success("This comment contains " + str(prediction[1]) + "% " + str(prediction[0]))
            # st.balloons()
        elif 60 < prediction[1] < 80:
            st.error("This might be a cyberbullying comment which contains " + str(prediction[1]) + "% " + str(
                prediction[0]))
        else:
            st.warning("This is not a cyberbullying comment")