import streamlit as st

USERS = {
    "patient@test.com": {
        "password": "1234",
        "role": "patient",
        "name": "John Doe"
    },
    "doctor@test.com": {
        "password": "1234",
        "role": "doctor",
        "name": "Dr. Smith"
    }
}

def login():

    st.markdown("## 🏥 DocTime")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        user = USERS.get(email)

        if user and user["password"] == password:

            st.session_state.logged_in = True
            st.session_state.role = user["role"]
            st.session_state.user = user

            st.rerun()

        else:
            st.error("Invalid credentials")


def logout():
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.user = None
    st.rerun()
