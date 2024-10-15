import streamlit as st
from PIL import Image
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

st.title("Certificate Validation System")
st.write("")
st.subheader("Select Your Role")

col1, col2 = st.columns(2)
institute_logo = Image.open("../assets/institute_logo.png")
with col1:
    st.image(institute_logo, output_format="jpg", width=230)
    clicked_institute = st.button("Institute")

company_logo = Image.open("../assets/company_logo.jpg")
with col2:
    st.image(company_logo, output_format="jpg", width=230)
    clicked_verifier = st.button("Verifier")

if clicked_institute:
    st.session_state.profile = "Institute"
    switch_page('login')
elif clicked_verifier:
    st.session_state.profile = "Verifier"
    switch_page('login')
