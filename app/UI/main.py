import streamlit as st
import requests
import time

# App config
st.set_page_config(page_title="Chat App", page_icon=":speech_balloon:", layout="wide")
st.title("🧠 RAG Chatbot")

# Session state initialization
if "history" not in st.session_state:
    st.session_state.history = []

# Feedback save handler
def save_feedback(index):
    st.session_state.history[index]["feedback"] = st.session_state[f"feedback_{index}"]

# Function to call streaming API
def stream_response(prompt):
    api_url = "http://localhost:8000/ask_qa"  # Change to your actual FastAPI endpoint

    try:
        response = requests.post(api_url, params={"query": prompt}, stream=True)
        if response.status_code != 200:
            st.error("Error: Unable to fetch response from the API.")
            return

        def generate():
            for chunk in response.iter_content(chunk_size=1, decode_unicode=True):
                if chunk:
                    yield chunk
        return generate()

    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
        return

# Render existing messages
for i, message in enumerate(st.session_state.history):
    with st.chat_message(message["role"]):
        st.write(message["content"])
        if message["role"] == "assistant":
            feedback = message.get("feedback", None)
            st.session_state[f"feedback_{i}"] = feedback

            st.feedback(
                "thumbs",
                key=f"feedback_{i}",
                disabled=feedback is not None,
                on_change=save_feedback,
                args=[i],
            )

# Get user input
prompt = st.chat_input("Say something")

if prompt:
    # Show user message
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.history.append({"role": "user", "content": prompt})

    # Show assistant message with streamed content
    with st.chat_message("assistant"):
        response_generator = stream_response(prompt)
        if response_generator:
            full_response = st.write_stream(response_generator)
            st.session_state.history.append({"role": "assistant", "content": full_response})
