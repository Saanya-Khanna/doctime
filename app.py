import streamlit as st
from patient import patient_dashboard
from doctor import doctor_dashboard

st.set_page_config(page_title="DocTime", layout="wide")

# SESSION STATE
if "user_type" not in st.session_state:
    st.session_state.user_type = "patient"

# ROUTING
if st.session_state.user_type == "patient":
    patient_dashboard()
else:
    doctor_dashboard()
