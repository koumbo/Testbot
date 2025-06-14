import streamlit as st
from streamlit_chat import message as st_message
import numpy as np
from run_model import run

if "chat_history_ids" not in st.session_state:
    st.session_state["chat_history_ids"] = None
if "book" not in st.session_state:
    st.session_state["book"] = []

txt = st.text_input("Type Here")

if txt:
    resp , hist = run(txt , st.session_state["chat_history_ids"])
    st.session_state["chat_history_ids"] = hist

    st.session_state["book"].append({"message" : txt ,
                                     "is_user" : True})
    st.session_state["book"].append({"message" : resp ,
                                     "is_user" : False})

for i , chat in enumerate(st.session_state["book"]):
    st_message(**chat , key = str(i))
