import streamlit as st
import base64
import time

# --- CONFIG ---
st.set_page_config(page_title="For Adekunle Mi", page_icon="❤️", layout="centered")

# --- LUXURY CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600&family=Quicksand:wght@300;500&display=swap');

    /* Custom Heart Cursor */
    html, body, * {
        cursor: url('https://cdn-icons-png.flaticon.com/32/2107/2107844.png'), auto;
    }

    /* Silk Gradient Background */
    .stApp {
        background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fbc2eb, #a18cd1);
        background-size: 400% 400%;
        animation: silkFlow 15s ease infinite;
    }
    @keyframes silkFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Typewriter Animation Effect */
    .typewriter-text {
        overflow: hidden;
        border-right: .15em solid #ff4d6d;
        white-space: pre-wrap;
        margin: 0 auto;
        letter-spacing: .10em;
        animation: typing 4s steps(40, end), blink-caret .75s step-end infinite;
        font-family: 'Quicksand', sans-serif;
        color: #4a0000;
        font-size: 1.15rem;
        line-height: 1.8;
    }

    @keyframes typing { from { max-height: 0; } to { max-height: 2000px; } }
    @keyframes blink-caret { from, to { border-color: transparent } 50% { border-color: #ff4d6d; } }

    /* Glassmorphism Letter Box */
    .letter-box {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 30px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 40px;
        box-shadow: 0 8px 32px 0 rgba(255, 77, 109, 0.2);
        margin-top: 20px;
    }

    /* Titles */
    h1 { font-family: 'Dancing Script', cursive; color: #d63031 !important; font-size: 4.5rem !important; text-shadow: 3px 3px 6px rgba(0,0,0,0.1); }
    h2 { font-family: 'Dancing Script', cursive; color: #b33939 !important; font-size: 3rem !important; }

    /* Floating Emojis */
    .emoji {
        position: fixed;
        font-size: 3.5rem;
        animation: floatUp 7s linear infinite;
        z-index: 999;
        pointer-events: none;
    }
    @keyframes floatUp {
        0% { transform: translateY(110vh) rotate(0deg); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(-20vh) rotate(360deg); opacity: 0; }
    }

    /* Luxury Envelope */
    .envelope-wrapper { display: flex; justify-content: center; padding: 40px; }
    .envelope {
        position: relative;
        width: 320px; height: 200px;
        background: #e53935;
        border-radius: 0 0 15px 15px;
        box-shadow: 0 25px 50px rgba(0,0,0,0.3);
    }
    .flap {
        position: absolute; top: 0; width: 0; height: 0;
        border-left: 160px solid transparent; border-right: 160px solid transparent;
        border-top: 130px solid #b71c1c;
        transform-origin: top; transition: transform 0.8s ease; z-index: 3;
    }
    .envelope:hover .flap { transform: rotateX(180deg); }
    .letter-peek {
        position: absolute; top: 10px; left: 20px; width: 280px; height: 160px;
        background: white; border-radius: 8px; z-index: 1;
        display: flex; justify-content: center; align-items: center;
        font-family: 'Dancing Script', cursive; font-size: 1.5rem; color: #b71c1c;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #ff4d6d, #d63031) !important;
        color: white !important;
        border-radius: 50px !important;
        border: none !important;
        padding: 12px 45px !important;
        font-weight: bold !important;
        box-shadow: 0 10px 20px rgba(214, 48, 49, 0.3) !important;
        transition: 0.4s !important;
    }
    .stButton>button:hover { transform: translateY(-3px) scale(1.05); box-shadow: 0 15px 25px rgba(214, 48, 49, 0.4) !important; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNCTIONS ---
def play_music():
    try:
        with open("ademi.mp3", "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            st.markdown(f'<audio autoplay loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>', unsafe_allow_html=True)
    except: pass

def spawn_emojis(emoji):
    import random
    for i in range(15):
        st.markdown(f'<div class="emoji" style="left:{i*7}vw; animation-delay:{random.uniform(0,6)}s;">{emoji}</div>', unsafe_allow_html=True)

# --- APP LOGIC ---
if 'page' not in st.session_state: st.session_state.page = 'welcome'

if st.session_state.page == 'welcome':
    st.markdown("<h1>Welcome Ade mii</h1>", unsafe_allow_html=True)
    spawn_emojis("❤️")
    if st.button("Next"):
        st.session_state.page = 'guess'
        st.rerun()

elif st.session_state.page == 'guess':
    play_music()
    st.markdown("<h2>A letter from yours truly...</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Guess who?</p>", unsafe_allow_html=True)
    name = st.text_input("", placeholder="Whose heart belongs to you?", key="name_box").lower().strip()
    if st.button("Unlock Love"):
        if name in ["adenroye", "kanyinsola", "tamilore", "mistura", "baby", "babe"]:
            st.session_state.page = 'pre_letter'
        else:
            st.session_state.page = 'wrong'
        st.rerun()

elif st.session_state.page == 'wrong':
    st.markdown("<h1>Really? 💔</h1>", unsafe_allow_html=True)
    spawn_emojis("💔")
    if st.button("Try Again"):
        st.session_state.page = 'guess'; st.rerun()

elif st.session_state.page == 'pre_letter':
    st.markdown("<h1>That is why I love you!</h1>", unsafe_allow_html=True)
    st.markdown('<div class="envelope-wrapper"><div class="envelope"><div class="flap"></div><div class="letter-peek">Open Me, Ade ❤️</div></div></div>', unsafe_allow_html=True)
    if st.button("Open Envelope"):
        st.session_state.page = 'the_letter'; st.rerun()

elif st.session_state.page == 'the_letter':
    st.markdown("<h2>Adekunle Mi,</h2>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="letter-box">
            <div class="typewriter-text">
Adekunle mi ,

I’ve been sitting with my thoughts for days, trying to find the right way to say everything that has been living in my heart. The truth is, no matter how I arrange these words, they will never fully capture how deeply I love you. But I hope you can feel my heart in every line. I love you. I love you in a way that has changed me. I care about you so much that sometimes it scares me, because your happiness truly matters to me. When you’re happy, I feel at peace. When you’re hurting, I feel it too. That’s how connected I feel to you. I don’t just want you for now. I want you for the rest of my life. I want to wake up beside you years from now and still feel butterflies. I want us to grow older together, to laugh about our struggles, to look back and say, “We really built this.” I see a future with you so clearly building our dreams side by side, pushing each other to be better, becoming successful together, creating wealth together, building a life that feels safe and full and blessed.

But before I talk about forever, I need to speak honestly about the past. I am truly sorry. I’m sorry for every time I hurt you, for the moments I let my actions disappoint you, for the pain I caused knowingly or unknowingly. I know I can’t erase those moments, and I can’t demand your forgiveness. But please believe me when I say I have reflected deeply. I have looked at myself. I have learned. I know trust is fragile. I know love needs to feel safe. And if I ever made you feel otherwise, I carry that regret heavily. All I’m asking is for a chance to prove that I am not the same person who made those mistakes. Growth is real. Change is real. And my love for you has never stopped being real.

Please find it in your heart to forgive me. Let’s not allow yesterday’s pain to steal tomorrow’s happiness. Let’s move forward. Open your heart to me again. Love me again the way you used to and I promise I will cherish it more carefully than ever before.

You mean more to me than pride, more than ego, more than the past. I choose you. I choose us. I choose the life we can build together. And if you let me, I will spend the rest of my life showing you just how much you are loved.
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Read More"):
        st.session_state.page = 'final'; st.rerun()

elif st.session_state.page == 'final':
    st.markdown("<h1>I love you Ade</h1>", unsafe_allow_html=True)
    spawn_emojis("💖")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Restart"): st.session_state.page = 'welcome'; st.rerun()
    with c2:
        if st.button("Quit"): st.markdown("<h3 style='text-align:center;'>Always yours. ❤️</h3>", unsafe_allow_html=True); st.stop()
