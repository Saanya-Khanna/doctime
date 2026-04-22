import streamlit as st

def patient_dashboard():

    st.title("Patient Dashboard")

    if "appointments" not in st.session_state:
        st.session_state.appointments = []

    specialty = st.selectbox(
        "Specialty",
        ["All", "Cardiologist", "Dermatologist", "Pediatrician"]
    )

    zipcode = st.text_input("Zip Code")

    doctors = [
        {"name": "Dr. Sarah", "specialty": "Cardiologist", "zip": "76013"},
        {"name": "Dr. Mike", "specialty": "Dermatologist", "zip": "75001"},
        {"name": "Dr. Priya", "specialty": "Pediatrician", "zip": "75201"},
    ]

    st.subheader("Doctors")

    for doc in doctors:

        if (specialty == "All" or doc["specialty"] == specialty) and (zipcode == "" or doc["zip"] == zipcode):

            st.markdown(f"""
            <div style="padding:12px; background:white; border-radius:10px; margin-bottom:10px;">
                <b>{doc['name']}</b><br>
                {doc['specialty']} • {doc['zip']}
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"Book {doc['name']}", key=doc["name"]):
                st.session_state.appointments.append(doc["name"])
                st.success("Booked!")
