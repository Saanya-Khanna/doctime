import streamlit as st
from components.ui import load_css, card

def doctor_dashboard():

    load_css()

    st.title("Doctor Dashboard")

    menu = st.sidebar.radio("Menu", ["Dashboard", "Schedule"])

    if menu == "Dashboard":
        card("Today's Patients", "5 appointments")

    elif menu == "Schedule":
        st.write("Manage availability here")

