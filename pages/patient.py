import streamlit as st
import api
from auth import logout
from components.ui import load_css, doctor_card
from datetime import datetime

DOCTORS = api.DOCTORS
get_availability = api.get_availability

def search_doctors(doctors, specialty, zipcode):

    results = []

    for doc in doctors:

        if (specialty == "All" or doc["specialty"] == specialty) and (zipcode == "" or zipcode in doc["zip"]):
            results.append(doc)

    return results


def patient_dashboard():

    load_css()

    with st.sidebar:
        st.title("Patient")
        if st.button("Logout"):
            logout()

    st.title("Find Doctors")

    # SEARCH BAR
    col1, col2 = st.columns(2)

    specialty = col1.selectbox(
        "Specialty",
        ["All", "Cardiologist", "Dermatologist", "Pediatrician"]
    )

    zipcode = col2.text_input("Zip Code")

    # SEARCH BUTTON (IMPORTANT FOR UX)
    if st.button("Search Doctors"):

        results = search_doctors(DOCTORS, specialty, zipcode)

        st.session_state.results = results

    # SHOW RESULTS
    if "results" in st.session_state:

        for doc in st.session_state.results:

            doctor_card(doc["name"], doc["specialty"], doc["zip"])

            # CLICK DOCTOR → SHOW PROFILE STYLE VIEW
            if st.button(f"View Availability - {doc['name']}", key=doc["id"]):

                st.session_state.selected_doctor = doc

    # -----------------------
    # DOCTOR DETAIL VIEW
    # -----------------------
    if "selected_doctor" in st.session_state:

        doc = st.session_state.selected_doctor

        st.markdown("---")
        st.subheader(f"{doc['name']} - Availability")

        schedule = get_availability(doc["id"])

        for slot in schedule:

            st.markdown(f"""
            <div class="card">
                📅 {slot['day']}<br>
                ⏰ {slot['time']}
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"Book {slot['time']}", key=f"{doc['id']}-{slot['time']}-{slot['day']}"):

                if "appointments" not in st.session_state:
                    st.session_state.appointments = []

                st.session_state.appointments.append({
                    "doctor": doc["name"],
                    "time": f"{slot['day']} {slot['time']}"
                })

                st.success("Appointment booked ✔")
