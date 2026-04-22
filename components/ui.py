import streamlit as st

def load_css():
    st.markdown("""
    <style>
    .card {
        background: white;
        padding: 18px;
        border-radius: 16px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.06);
        margin-bottom: 15px;
    }

    .stApp {
        background: linear-gradient(180deg, #F6F9FC, #EEF4FF);
    }

    .stButton > button {
        background: #2F80ED;
        color: white;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)


def card(title, subtitle=""):
    st.markdown(f"""
    <div class="card">
        <h4>{title}</h4>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

