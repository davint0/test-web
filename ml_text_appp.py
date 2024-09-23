import streamlit as st
import pickle

with open('model_pipeline.pkl', 'rb') as model_file:
    model_pipeline = pickle.load(model_file)


def run_ml_text_app():
    st.subheader('Machine Learning Section')

    st.title("Fake News Detection")
    st.write("This model uses Lemmatization as Data Preprocessing, TF-IDF as Feature Engineering and XGBoost for Accuracy.")

    input_title = st.text_area("Enter the title of the news article:")
    input_text = st.text_area("Enter the text of the news article:")

    if st.button("Classify"):
        # Combine title and text for prediction
        combined_input = input_title + " " + input_text

        combined_input = [combined_input]

        prediction = model_pipeline.predict(combined_input)

        # Show the result
        st.write(f"Prediction: {'Fake News' if prediction == 1 else 'Real News'}")


