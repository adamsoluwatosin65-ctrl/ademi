import streamlit as st
import base64

# --- CONFIG ---
st.set_page_config(page_title="For Adekunle Mi", page_icon="❤️", layout="centered")

# --- LUXURY CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600&family=Quicksand:wght@300;500&display=swap');

    html, body, * {
        cursor: url('https://cdn-icons-png.flaticon.com/32/2107/2107844.png'), auto !important;
    }

    .stApp {
        background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fbc2eb, #a18cd1);
        background-size: 400% 400%;
        animation: silkFlow 12s ease infinite;
    }
    @keyframes silkFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Auto-Opening Envelope Animation */
    @keyframes autoOpen {
        0% { transform: rotateX(0deg); }
        100% { transform: rotateX(180deg); }
    }

    .envelope-wrapper { 
        display: flex; 
        justify-content: center; 
        padding: 50px 0; 
    }

    .envelope {
        position: relative;
        width: 400px; /* Bigger Width */
        height: 260px; /* Bigger Height */
        background: #e53935;
        border-radius: 0 0 15px 15px;
        box-shadow: 0 40px 80px rgba(0,0,0,0.4);
    }

    .flap {
        position: absolute; 
        top: 0; 
        width: 0; 
        height: 0;
        border-left: 200px solid transparent; 
        border-right: 200px solid transparent;
        border-top: 160px solid #b71c1c;
        transform-origin: top; 
        z-index: 3;
        /* Animation triggers automatically after 1 second delay */
        animation: autoOpen 1.5s ease-in-out forwards;
        animation-delay: 1s; 
    }

    .letter-peek {
        position: absolute; 
        top: 15px; 
        left: 20px; 
        width: 360px; 
        height: 220px;
        background: white; 
        border-radius: 8px; 
        z-index: 1;
        display: flex; 
        justify-content: center; 
        align-items: center;
        font-family: 'Dancing Script', cursive; 
        font-size: 2rem; 
        color: #b71c1c;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }

    /* Rest of Styling */
    .typewriter {
        overflow: hidden;
        white-space: pre-wrap;
        margin: 0 auto;
        animation: typing 6s steps(100, end);
        font-family: 'Quicksand', sans-serif;
        font-size: 1.15rem;
        line-height: 1.8;
        color: #4a0000;
    }
    @keyframes typing { from { max-height: 0; } to { max-height: 3000px; } }

    .glass-card {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 30px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 40px;
    }

    .emoji {
        position: fixed; font-size: 3.5rem;
        animation: floatUp 7s linear infinite;
        z-index: 999; pointer-events: none;
    }
    @keyframes floatUp {
        0% { transform: translateY(110vh) rotate(0deg); opacity: 0; }
        20% { opacity: 1; }
        100% { transform: translateY(-20vh) rotate(360deg); opacity: 0; }
    }

    h1 { font-family: 'Dancing Script', cursive; color: #d63031 !important; font-size: 4rem !important; text-align: center; }
    .stButton>button {
        background: linear-gradient(135deg, #ff4d6d, #d63031) !important;
        color: white !important; border-radius: 50px !important;
        padding: 15px 50px !important; display: block; margin: 0 auto;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUNCTIONS ---
def play_audio():
    try:
        with open("ademi.mp3", "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            st.markdown(f'<audio autoplay loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>', unsafe_allow_html=True)
    except: pass

def spawn_emojis(emoji_char):
    import random
    for i in range(18):
        st.markdown(f'<div class="emoji" style="left:{i*5.5}vw; animation-delay:{random.uniform(0,6)}s;">{emoji_char}</div>', unsafe_allow_html=True)

# --- LOGIC ---
if 'page' not in st.session_state: st.session_state.page = 'welcome'
if 'music' not in st.session_state: st.session_state.music = False

if st.session_state.music:
    play_audio()

# --- PAGES ---
if st.session_state.page == 'welcome':
    st.markdown("<h1>Welcome Ade mii</h1>", unsafe_allow_html=True)
    spawn_emojis("❤️")
    if st.button("Next"):
        st.session_state.music = True
        st.session_state.page = 'guess'
        st.rerun()

elif st.session_state.page == 'guess':
    st.markdown("<h1>A letter from yours truly...</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Guess who?</h3>", unsafe_allow_html=True)
    name = st.text_input("", placeholder="Enter name...", key="name_box").lower().strip()
    if st.button("Submit"):
        if name in ["adenroye", "kanyinsola", "tamilore", "mistura", "baby", "babe"]:
            st.session_state.page = 'success'
        else:
            st.session_state.page = 'wrong'
        st.rerun()

elif st.session_state.page == 'wrong':
    st.markdown("<h1>Really? 💔</h1>", unsafe_allow_html=True)
    spawn_emojis("💔")
    if st.button("Try Again"):
        st.session_state.page = 'guess'; st.rerun()

elif st.session_state.page == 'success':
    st.markdown("<h1>That is why I love you!</h1>", unsafe_allow_html=True)
    # The Envelope now opens automatically via CSS animation
    st.markdown("""
        <div class="envelope-wrapper">
            <div class="envelope">
                <div class="flap"></div>
                <div class="letter-peek">For Adekunle ❤️</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("✉️ Click to Read"):
        st.session_state.page = 'letter'; st.rerun()

elif st.session_state.page == 'letter':
    st.markdown(f"""
        <div class='glass-card'>
            <div class='typewriter'>
            Adekunle mi ,<br><br>
            I’ve been sitting with my thoughts for days, trying to find the right way to say everything that has been living in my heart. The truth is, no matter how I arrange these words, they will never fully capture how deeply I love you. But I hope you can feel my heart in every line. I love you. I love you in a way that has changed me. I care about you so much that sometimes it scares me, because your happiness truly matters to me. When you’re happy, I feel at peace. When you’re hurting, I feel it too. That’s how connected I feel to you. I don’t just want you for now. I want you for the rest of my life. I want to wake up beside you years from now and still feel butterflies. I want us to grow older together, to laugh about our struggles, to look back and say, “We really built this.” I see a future with you so clearly building our dreams side by side, pushing each other to be better, becoming successful together, creating wealth together, building a life that feels safe and full and blessed.<br><br>
            But before I talk about forever, I need to speak honestly about the past. I am truly sorry. I’m sorry for every time I hurt you, for the moments I let my actions disappoint you, for the pain I caused knowingly or unknowingly. I know I can’t erase those moments, and I can’t demand your forgiveness. But please believe me when I say I have reflected deeply. I have looked at myself. I have learned. I know trust is fragile. I know love needs to feel safe. And if I ever made you feel otherwise, I carry that regret heavily. All I’m asking is for a chance to prove that I am not the same person who made those mistakes. Growth is real. Change is real. And my love for you has never stopped being real.<br><br>
            Please find it in your heart to forgive me. Let’s not allow yesterday’s pain to steal tomorrow’s happiness. Let’s move forward. Open your heart to me again. Love me again the way you used to and I promise I will cherish it more carefully than ever before.<br><br>
            You mean more to me than pride, more than ego, more than the past. I choose you. I choose us. I choose the life we can build together. And if you let me, I will spend the rest of my life showing you just how much you are loved.
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Next"):
        st.session_state.page = 'final'; st.rerun()

elif st.session_state.page == 'final':
    st.markdown("<h1>I love you Ade</h1>", unsafe_allow_html=True)
    spawn_emojis("💖")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Restart"): st.session_state.page = 'welcome'; st.rerun()
    with c2:
        if st.button("Quit"):
            st.session_state.music = False
            st.markdown("<h2 style='text-align:center;'>Goodbye, My Love.</h2>", unsafe_allow_html=True)
            st.stop()
