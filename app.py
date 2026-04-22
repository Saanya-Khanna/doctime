import streamlit as st
from auth import login
from pages.patient import patient_dashboard
from pages.doctor import doctor_dashboard
from components.ui import load_css

st.set_page_config(page_title="DocTime", layout="wide")

load_css()

# INIT STATE
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None

# ROUTING
if not st.session_state.logged_in:
    login()

else:
    if st.session_state.role == "patient":
        patient_dashboard()
    else:
        doctor_dashboard()
