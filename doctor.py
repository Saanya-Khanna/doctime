import streamlit as st

def doctor_dashboard():

    st.title("Doctor Dashboard 👨‍⚕️")

    if "appointments" not in st.session_state:
        st.session_state.appointments = []

    st.subheader("Today's Appointments")

    if st.session_state.appointments:
        for appt in st.session_state.appointments:
            st.markdown(f"""
            <div style="
                background:white;
                padding:12px;
                border-radius:10px;
                margin-bottom:10px;
            ">
                Patient: {appt}<br>
                Time: 10:00 AM
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No appointments yet.")
