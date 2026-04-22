import streamlit as st
from auth import logout
from components.ui import load_css

def doctor_dashboard():

    load_css()

    with st.sidebar:
        st.title("Doctor Portal")

        if st.button("Logout"):
            logout()

    st.title("Doctor Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Today", "5 appointments")
    col2.metric("Patients", "32")
    col3.metric("Rating", "4.8 ⭐")

    st.markdown("---")

    st.subheader("Today's Schedule")

    if "appointments" in st.session_state and st.session_state.appointments:

        for a in st.session_state.appointments:
            st.markdown(f"""
            <div class="card">
                Patient: John Doe<br>
                Appointment: 10:00 AM
            </div>
            """, unsafe_allow_html=True)

    else:
        st.info("No appointments today")
