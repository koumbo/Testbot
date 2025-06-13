import streamlit as st
from streamlit_chat import message as st_message
from run_model import run  # Ensure this import is correct

# Initialize session state
if "chat_history_ids" not in st.session_state:
    st.session_state["chat_history_ids"] = None
if "book" not in st.session_state:
    st.session_state["book"] = []

# User input
txt = st.text_input("Type Here")

if txt:
    try:
        # Get model response
        resp, hist = run(txt, st.session_state["chat_history_ids"])
        st.session_state["chat_history_ids"] = hist

        # Update chat history
        st.session_state["book"].append({"message": txt, "is_user": True})
        st.session_state["book"].append({"message": resp, "is_user": False})
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Display chat history
for i, chat in enumerate(st.session_state["book"]):
    st_message(**chat, key=str(i))
