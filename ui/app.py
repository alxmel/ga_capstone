""" Streamlit frontend """
import streamlit as st
import random
import time
import requests
from demo import SAMPLE_REQUEST

# Streamlit default port is 8501
BASE_URL = "http://127.0.0.1:8000"

# Stream response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

def get_health(base_url: str):
    """ Performs Health Check on the backend API server """
    response = requests.get(f"{base_url}/health")

    for letter in "The status of the backend API server is: ".split():
        yield letter + ' '
        time.sleep(0.05)
    for letter in response.json()["status"]:
        yield f":green[{letter}]"
        time.sleep(0.05)


def get_prediction(base_url: str, sample_request: dict):
    """ Performs a Prediction """
    response = requests.post(
        url=f"{base_url}/predict",
        json=sample_request
    ).json()

    for word in "The predicted next state is: ".split():
        yield word + ' '
        time.sleep(0.05)
    for letter in response["prediction_label"]:
        yield f":red[{letter}]"
        time.sleep(0.05)

    yield "\n\n"

    for word in "With a probability of: ".split():
        yield word + ' '
        time.sleep(0.05)
    for letter in str(response["probabilities"].get(response["prediction_label"])):
        yield f":blue[{letter}]"
        time.sleep(0.05)



st.title("GA Capstone!")

# Initialize the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Displaying chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Enter chat"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        if prompt == "healthcheck":
            response = st.write_stream(get_health(BASE_URL))
        elif prompt == "predict":
            response = st.write_stream(get_prediction(BASE_URL, SAMPLE_REQUEST))
        else:
            response = st.write_stream(response_generator())
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
