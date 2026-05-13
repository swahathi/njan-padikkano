import streamlit as st
import pandas as pd
import random
from datetime import datetime
from model import predict_study

# ── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Njan Padikkano?", layout="centered")

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;700&display=swap');

*, body { box-sizing: border-box; margin: 0; padding: 0; }

.stApp {
    background: linear-gradient(135deg, #FFCDC9 0%, #ffb3ae 100%);
    min-height: 100vh;
    display: flex; align-items: center; justify-content: center;
}

#MainMenu, footer, header { visibility: hidden; }

/* ── TITLE ── */
.big-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(4rem, 14vw, 9rem);
    color: #1a1a1a;
    text-align: center;
    letter-spacing: 0.04em;
    line-height: 1;
    text-shadow: 4px 4px 0px rgba(0,0,0,0.12);
    animation: fadeDown 0.6s ease both;
}

/* ── RESULT TEXT ── */
.result-text {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(2.5rem, 8vw, 5rem);
    color: #1a1a1a;
    text-align: center;
    letter-spacing: 0.05em;
    margin-top: 1.5rem;
    animation: fadeUp 0.5s ease both;
}

/* ── BUTTON ── */
div.stButton { display: flex; justify-content: center; margin-top: 2.5rem; }
div.stButton > button {
    background: #1a1a1a !important;
    color: #FFCDC9 !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 0.9rem 3.2rem !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 1rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.08em !important;
    cursor: pointer !important;
    transition: transform 0.15s ease, opacity 0.15s ease !important;
    box-shadow: 0 4px 20px rgba(0,0,0,0.18) !important;
}
div.stButton > button:hover {
    transform: scale(1.05) !important;
    opacity: 0.92 !important;
}

/* ── IMAGE ── */
div[data-testid="stImage"] { display: flex; justify-content: center; }
div[data-testid="stImage"] img {
    border-radius: 16px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.18);
    animation: pop 0.4s cubic-bezier(.34,1.56,.64,1) both;
}

/* ── ANIMATIONS ── */
@keyframes fadeDown {
    from { opacity: 0; transform: translateY(-24px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(24px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes pop {
    from { opacity: 0; transform: scale(0.85); }
    to   { opacity: 1; transform: scale(1); }
}
</style>
""", unsafe_allow_html=True)




# ── MEMES ─────────────────────────────────────────────────────────────────────
STUDY_MEMES  = ["memes/study1.jpeg","memes/study2.jpeg","memes/study3.jpeg","memes/study4.jpeg","memes/study5.GIF","memes/study6.GIF","memes/study7.GIF","memes/study8.GIF"]
RELAX_MEMES  = ["memes/relax1.jpeg", "memes/relax2.jpeg","memes/relax3.jpeg","memes/relax4.jpeg","memes/relax5.GIF","memes/relax6.GIF"]

# ── STATE ─────────────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "home"

# ── HOME ──────────────────────────────────────────────────────────────────────
if st.session_state.page == "home":
    st.markdown("<div class='big-title'>NJAN<br>PADIKKANO?</div>", unsafe_allow_html=True)

    if st.button("TELL ME"):
        hour = datetime.now().hour
        rand = random.randint(0, 10)

        pred = predict_study(hour, rand)

        st.session_state.meme = random.choice(STUDY_MEMES if pred else RELAX_MEMES)
        st.session_state.text = "LOCK IN GANG!!! " if pred else "Naaale avattee "
        st.session_state.page = "result"
        st.rerun()

# ── RESULT ────────────────────────────────────────────────────────────────────
elif st.session_state.page == "result":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(st.session_state.meme, width=400)

    st.markdown(f"<div class='result-text'>{st.session_state.text}</div>", unsafe_allow_html=True)

    if st.button("↩ BACK"):
        st.session_state.page = "home"
        st.rerun()




