import streamlit as st

from auth import login
from patient import patient_dashboard
from doctor import doctor_dashboard

st.set_page_config(page_title="DocTime", layout="wide")

# -----------------------
# SESSION INIT
# -----------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None


# -----------------------
# APP ROUTING
# -----------------------
if not st.session_state.logged_in:
    login()

else:
    if st.session_state.role == "patient":
        patient_dashboard()
    else:
        doctor_dashboard()
