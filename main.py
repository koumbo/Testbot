#import libraries
import streamlit as st
from streamlit_chat import message as st_message
import numpy as np
from run_model import run_bot

# Initialize session state variables if they don't exist
st.session_state.setdefault("chat_history_ids", None)
st.session_state.setdefault("book", [])

# Text input for user interaction
txt = st.text_input("Type Here")

if txt:
    # Generate bot response and update chat history
    resp , hist = run_bot(txt , st.session_state["chat_history_ids"])
    st.session_state["chat_history_ids"] = hist
    # Append user and bot messages to the chat history
    st.session_state["book"].append({"message": txt,"is_user" : True})
    st.session_state["book"].append({"message": resp,"is_user" : False})

# Display the chat history
for i , chat in enumerate(st.session_state["book"]):
    st_message(**chat , key = str(i))
 

