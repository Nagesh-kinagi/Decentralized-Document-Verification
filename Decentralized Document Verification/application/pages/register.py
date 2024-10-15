import streamlit as st
from db.firebase_app import register
from streamlit_extras.switch_page_button import switch_page
def hide_icons():
    hide_css = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """
    st.markdown(hide_css, unsafe_allow_html=True)

def hide_sidebar():
    st.markdown("<style>div.css-1l02zno{visibility:hidden;}</style>", unsafe_allow_html=True)

def remove_whitespaces():
    st.markdown("<style>div.row-widget.stRadio {flex-direction: row;}</style>", unsafe_allow_html=True)

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_icons()
hide_sidebar()
remove_whitespaces()

form = st.form("login")
email = form.text_input("Enter your email")
password = form.text_input("Enter your password", type="password")
clicked_login = st.button("Already registered? Click here to login!")

if clicked_login:
    switch_page("login")
    
submit = form.form_submit_button("Register")
if submit:
    result = register(email, password)
    if result == "success":
        st.success("Registration successful!")
        if st.session_state.profile == "Institute":
            switch_page("institute")
        else:
            switch_page("verifier")
    else:
        st.error("Registration unsuccessful!")