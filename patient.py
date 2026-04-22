import streamlit as st
from auth import logout

from components.ui import load_css, card

def patient_dashboard():

    load_css()

    if st.sidebar.button("Logout"):
    logout()

    st.title("Patient Dashboard")

    if "appointments" not in st.session_state:
        st.session_state.appointments = []

    menu = st.sidebar.radio("Menu", ["Dashboard", "Search", "Appointments"])

    if menu == "Dashboard":
        card("Book Appointment", "Find doctors near you")

    elif menu == "Search":
        st.subheader("Search Doctors")

        if st.button("Book Dr. Smith"):
            st.session_state.appointments.append("Dr. Smith at 10AM")

    elif menu == "Appointments":
        for a in st.session_state.appointments:
            card("Appointment", a)

