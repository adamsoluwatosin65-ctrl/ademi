import streamlit as st
import base64

# --- CONFIG ---
st.set_page_config(page_title="For Ade Mii", page_icon="❤️", layout="centered")

# --- CUSTOM CSS (Animations & Envelope) ---
st.markdown("""
    <style>
    /* Global Styles */
    .stApp {
        background-color: #fff0f3;
    }
    h1, h2, h3, p {
        color: #ff4d6d ! embarrassment;
        text-align: center;
    }

    /* Floating Emoji Animation */
    @keyframes floatUp {
        0% { transform: translateY(100vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(-100vh) rotate(360deg); opacity: 0; }
    }
    .emoji {
        position: fixed;
        bottom: -10vh;
        font-size: 2rem;
        animation: floatUp 5s linear infinite;
        z-index: 0;
    }

    /* Envelope CSS */
    .envelope-container {
        position: relative;
        width: 250px;
        height: 180px;
        background: #ff4d6d;
        margin: 50px auto;
        border-radius: 0 0 10px 10px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    .envelope-flap {
        position: absolute;
        top: 0;
        width: 0;
        height: 0;
        border-left: 125px solid transparent;
        border-right: 125px solid transparent;
        border-top: 100px solid #c9184a;
        z-index: 3;
        transition: transform 0.8s ease;
        transform-origin: top;
    }
    .envelope-container:hover .envelope-flap {
        transform: rotateX(180deg);
    }
    .letter-paper {
        position: absolute;
        top: 10px;
        left: 25px;
        width: 200px;
        height: 120px;
        background: white;
        z-index: 1;
        display: flex;
        justify-content: center;
        align-items: center;
        font-family: 'Georgia', serif;
        color: #ff4d6d;
        border-radius: 5px;
    }

    /* Buttons */
    .stButton>button {
        display: block;
        margin: 0 auto;
        border-radius: 30px;
        background-color: #ff4d6d;
        color: white;
        border: none;
        padding: 10px 40px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HELPER FUNCTIONS ---
def play_audio():
    """Encodes and plays the ademi.mp3 file"""
    try:
        with open("ademi.mp3", "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            audio_html = f"""
                <audio autoplay loop>
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
            """
            st.markdown(audio_html, unsafe_allow_html=True)
    except:
        st.warning("Add 'ademi.mp3' to the folder to hear the music! 🎵")

def spawn_emojis(type="❤️"):
    """Creates multiple floating emojis"""
    for i in range(15):
        pos = i * 7
        delay = i * 0.4
        st.markdown(f'<div class="emoji" style="left:{pos}vw; animation-delay:{delay}s;">{type}</div>', unsafe_allow_html=True)

# --- SESSION STATE ---
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# --- PAGE LOGIC ---

# 1. WELCOME PAGE
if st.session_state.page == 'welcome':
    st.write("# Welcome Ade mii")
    spawn_emojis("❤️")
    if st.button("Next"):
        st.session_state.page = 'guess'
        st.rerun()

# 2. GUESS WHO PAGE
elif st.session_state.page == 'guess':
    play_audio()
    st.write("## A letter from yours truly...")
    st.write("### Guess who?")
    name = st.text_input("Enter your name:", placeholder="Type here...", key="name_box").lower().strip()
    
    if st.button("Confirm"):
        allowed = ["adenroye", "kanyinsola", "tamilore", "mistura", "baby", "babe"]
        if name in allowed:
            st.session_state.page = 'love_reason'
        else:
            st.session_state.page = 'wrong_name'
        st.rerun()

# 3. WRONG NAME PAGE
elif st.session_state.page == 'wrong_name':
    st.write("# Really? 💔")
    spawn_emojis("💔")
    if st.button("Try Again"):
        st.session_state.page = 'guess'
        st.rerun()

# 4. THAT IS WHY I LOVE YOU PAGE
elif st.session_state.page == 'love_reason':
    st.write("# That is why I love you!")
    st.markdown("""
        <div class="envelope-container">
            <div class="envelope-flap"></div>
            <div class="letter-paper">For Ade ✉️</div>
        </div>
    """, unsafe_allow_html=True)
    st.write("*(Hover over the envelope, then click open)*")
    if st.button("Open"):
        st.session_state.page = 'the_letter'
        st.rerun()

# 5. THE MESSAGE PAGE
elif st.session_state.page == 'the_letter':
    st.markdown("""
    ### My Dearest Ade,
    
    In a world full of billions, my heart chose you. You aren't just a name or a person to me; 
    you are the melody in my favorite song and the peace at the end of a long day. 
    
    I wrote this little website just to remind you that you are loved beyond words, 
    beyond code, and beyond distance. Every time you see this, know that I am 
    grateful for every smile you've given me.
    
    Forever yours,  
    **Yours Truly**
    """)
    if st.button("Next"):
        st.session_state.page = 'final'
        st.rerun()

# 6. FINAL PAGE
elif st.session_state.page == 'final':
    st.write("# I love you Ade")
    spawn_emojis("💖")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Restart"):
            st.session_state.page = 'welcome'
            st.rerun()
    with col2:
        if st.button("Quit"):
            st.write("### Goodbye, Ade mii. ❤️")
            st.stop()