import streamlit as st
import base64

# --- CONFIG ---
st.set_page_config(page_title="For Adekunle Mi", page_icon="❤️", layout="centered")

# --- ADVANCED BEAUTIFUL CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600&family=Quicksand:wght@300;500&display=swap');

    /* Animated Gradient Background */
    .stApp {
        background: linear-gradient(-45deg, #ffafbd, #ffc3a0, #ffafbd, #ffc3a0);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Fine Fonts */
    h1 { font-family: 'Dancing Script', cursive; color: #d63031 !important; font-size: 4rem !important; text-shadow: 2px 2px 4px rgba(0,0,0,0.1); }
    h2, h3, p, div { font-family: 'Quicksand', sans-serif; color: #b33939; font-weight: 500; }

    /* Visible Flying Emojis */
    @keyframes floatUp {
        0% { transform: translateY(110vh) scale(0.5); opacity: 0; }
        20% { opacity: 1; }
        100% { transform: translateY(-20vh) scale(1.5); opacity: 0; }
    }
    .emoji {
        position: fixed;
        font-size: 3rem; /* Bigger Emojis */
        animation: floatUp 6s linear infinite;
        z-index: 999;
        pointer-events: none;
    }

    /* Big Beautiful Envelope */
    .envelope-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 300px;
    }
    .envelope {
        position: relative;
        width: 350px; /* Much Bigger */
        height: 230px;
        background: #ef5350;
        border-radius: 0 0 15px 15px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    }
    .flap {
        position: absolute;
        top: 0;
        width: 0;
        height: 0;
        border-left: 175px solid transparent;
        border-right: 175px solid transparent;
        border-top: 140px solid #d32f2f;
        transform-origin: top;
        transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        z-index: 3;
    }
    .envelope:hover .flap {
        transform: rotateX(180deg);
    }
    .letter-inside {
        position: absolute;
        top: 10px;
        left: 25px;
        width: 300px;
        height: 180px;
        background: #fff;
        border-radius: 10px;
        z-index: 1;
        display: flex;
        justify-content: center;
        align-items: center;
        font-family: 'Dancing Script', cursive;
        font-size: 1.8rem;
        color: #d32f2f;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.05);
    }

    /* Elegant Letter Box */
    .letter-box {
        background: rgba(255, 255, 255, 0.9);
        padding: 40px;
        border-radius: 25px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        font-size: 1.2rem;
        line-height: 1.8;
        border: 2px solid #ffafbd;
    }

    /* Buttons */
    .stButton>button {
        background: #d32f2f;
        color: white;
        border-radius: 50px;
        padding: 15px 50px;
        font-size: 1.2rem;
        border: none;
        box-shadow: 0 4px 15px rgba(211, 47, 47, 0.4);
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: #b71c1c;
    }
    </style>
    """, unsafe_allow_html=True)

# --- AUDIO LOGIC ---
def play_audio():
    try:
        with open("ademi.mp3", "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            st.markdown(f'<audio autoplay loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>', unsafe_allow_html=True)
    except:
        pass

# --- EMOJI SPAWNER ---
def spawn_emojis(emoji_char):
    import random
    for i in range(20):
        left = i * 5
        delay = random.uniform(0, 5)
        st.markdown(f'<div class="emoji" style="left:{left}vw; animation-delay:{delay}s;">{emoji_char}</div>', unsafe_allow_html=True)

# --- NAVIGATION ---
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# --- PAGES ---
if st.session_state.page == 'welcome':
    st.markdown("<h1>Welcome Ade mii</h1>", unsafe_allow_html=True)
    spawn_emojis("❤️")
    if st.button("Next"):
        st.session_state.page = 'guess'
        st.rerun()

elif st.session_state.page == 'guess':
    play_audio()
    st.markdown("<h2>A letter from yours truly...</h2>", unsafe_allow_html=True)
    st.markdown("### Guess who?")
    name = st.text_input("", placeholder="Enter name here...", key="name_box").lower().strip()
    if st.button("Open My Heart"):
        valid = ["adenroye", "kanyinsola", "tamilore", "mistura", "baby", "babe"]
        if name in valid:
            st.session_state.page = 'success'
        else:
            st.session_state.page = 'wrong'
        st.rerun()

elif st.session_state.page == 'wrong':
    st.markdown("<h1>Really? 💔</h1>", unsafe_allow_html=True)
    spawn_emojis("💔")
    if st.button("Please Try Again"):
        st.session_state.page = 'guess'
        st.rerun()

elif st.session_state.page == 'success':
    st.markdown("<h1>That is why I love you!</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div class="envelope-wrapper">
            <div class="envelope">
                <div class="flap"></div>
                <div class="letter-inside">For Adekunle ❤️</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Hover to see it open!</p>", unsafe_allow_html=True)
    if st.button("Open Now"):
        st.session_state.page = 'letter_page'
        st.rerun()

elif st.session_state.page == 'letter_page':
    st.markdown("<h2>My Dearest Adekunle</h2>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="letter-box">
        Adekunle mi ,<br><br>
        I’ve been sitting with my thoughts for days, trying to find the right way to say everything that has been living in my heart. 
        The truth is, no matter how I arrange these words, they will never fully capture how deeply I love you. 
        But I hope you can feel my heart in every line. I love you. I love you in a way that has changed me. 
        I care about you so much that sometimes it scares me, because your happiness truly matters to me. 
        When you’re happy, I feel at peace. When you’re hurting, I feel it too. That’s how connected I feel to you. 
        I don’t just want you for now. I want you for the rest of my life. I want to wake up beside you years from now and still feel butterflies. 
        I want us to grow older together, to laugh about our struggles, to look back and say, “We really built this.” 
        I see a future with you so clearly building our dreams side by side, pushing each other to be better, becoming successful together, 
        creating wealth together, building a life that feels safe and full and blessed.<br><br>
        But before I talk about forever, I need to speak honestly about the past. I am truly sorry. 
        I’m sorry for every time I hurt you, for the moments I let my actions disappoint you, for the pain I caused knowingly or unknowingly. 
        I know I can’t erase those moments, and I can’t demand your forgiveness. But please believe me when I say I have reflected deeply. 
        I have looked at myself. I have learned. I know trust is fragile. I know love needs to feel safe. 
        And if I ever made you feel otherwise, I carry that regret heavily. All I’m asking is for a chance to prove that I am not the same person 
        who made those mistakes. Growth is real. Change is real. And my love for you has never stopped being real.<br><br>
        Please find it in your heart to forgive me. Let’s not allow yesterday’s pain to steal tomorrow’s happiness. Let’s move forward. 
        Open your heart to me again. Love me again the way you used to and I promise I will cherish it more carefully than ever before.<br><br>
        You mean more to me than pride, more than ego, more than the past. I choose you. I choose us. 
        I choose the life we can build together. And if you let me, I will spend the rest of my life showing you just how much you are loved.
        </div>
    """, unsafe_allow_html=True)
    if st.button("Read More"):
        st.session_state.page = 'final'
        st.rerun()

elif st.session_state.page == 'final':
    st.markdown("<h1>I love you Ade</h1>", unsafe_allow_html=True)
    spawn_emojis("💖")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Restart"):
            st.session_state.page = 'welcome'
            st.rerun()
    with col2:
        if st.button("Quit"):
            st.markdown("### Always & Forever ❤️")
            st.stop()
