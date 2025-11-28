import streamlit as st
from openai import OpenAI

st.title("💬 Chatbot")

# Load API key from Streamlit Cloud secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display previous messages
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Save user message
    st.session_state["messages"].append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # Call OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state["messages"]
    )

    bot_reply = response.choices[0].message["content"]

    # Save bot reply
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})

    with st.chat_message("assistant"):
        st.write(bot_reply)
