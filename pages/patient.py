import streamlit as st
from auth import logout
from api import fetch_doctors
from components.ui import load_css, doctor_card

def patient_dashboard():

    load_css()

    with st.sidebar:
        st.title("Patient")
        if st.button("Logout"):
            logout()

def search_doctors(doctors, specialty, zipcode):

    results = []

    for doc in doctors:

        match_specialty = (specialty == "All" or doc["specialty"] == specialty)
        match_zip = (zipcode == "" or zipcode in doc["zip"])

        if match_specialty and match_zip:
            results.append(doc)

    return results


    # REAL API CALL
    doctors = fetch_doctors(specialty, zipcode)

    if not doctors:
        st.info("No doctors found. Try different filters.")
        return

    st.subheader(f"Available Doctors ({len(doctors)})")

    # DISPLAY DOCTORS
    for doc in doctors:

        doctor_card(doc["name"], doc["specialty"], doc["zip"])

        if st.button(f"Book {doc['name']}", key=doc["name"]):

            st.session_state.appointments.append({
                "doctor": doc["name"],
                "time": "10:00 AM (demo)"
            })

            st.success("Appointment booked ✔")

    st.markdown("---")

    # APPOINTMENTS
    st.subheader("Your Appointments")

    for a in st.session_state.appointments:
        st.markdown(f"""
        <div class="card">
            <b>{a['doctor']}</b><br>
            {a['time']}
        </div>
        """, unsafe_allow_html=True)
