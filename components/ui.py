import streamlit as st

def load_css():
    st.markdown("""
    <style>

    /* Background */
    .stApp {
        background-color: #F7F8FA;
        font-family: 'Inter', sans-serif;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #0F172A;
        color: white;
    }

    /* Card (Zocdoc style) */
    .card {
        background: white;
        border-radius: 16px;
        padding: 18px;
        margin-bottom: 14px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.06);
        border: 1px solid rgba(0,0,0,0.05);
        transition: all 0.2s ease;
    }

    .card:hover {
        transform: translateY(-2px);
        box-shadow: 0 14px 30px rgba(0,0,0,0.10);
    }

    /* Primary Button */
    .stButton > button {
        background: linear-gradient(135deg, #2563EB, #3B82F6);
        color: white;
        border-radius: 10px;
        padding: 10px 14px;
        border: none;
        font-weight: 500;
        width: 100%;
    }

    /* Headings */
    h1, h2, h3 {
        color: #0F172A;
    }

    /* Subtext */
    p {
        color: #64748B;
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
