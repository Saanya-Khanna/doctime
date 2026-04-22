import streamlit as st

def load_css():

    st.markdown("""
    <style>

    .stApp {
        background-color: #F6F8FB;
        font-family: Inter, sans-serif;
    }

    section[data-testid="stSidebar"] {
        background-color: #0F172A;
        color: white;
    }

    .card {
        background: white;
        padding: 18px;
        border-radius: 16px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        margin-bottom: 12px;
        border: 1px solid rgba(0,0,0,0.05);
    }

    .stButton > button {
        background: linear-gradient(135deg, #2563EB, #3B82F6);
        color: white;
        border-radius: 10px;
        width: 100%;
        padding: 10px;
    }

    </style>
    """, unsafe_allow_html=True)


def doctor_card(name, specialty, zip_code):

    st.markdown(f"""
    <div class="card">
        <h3>🧑‍⚕️ {name}</h3>
        <p>{specialty} • 📍 {zip_code}</p>
    </div>
    """, unsafe_allow_html=True)
