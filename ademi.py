import streamlit as st
import base64

# --- CONFIG ---
st.set_page_config(page_title="For Adekunle Mi", page_icon="❤️", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp {
        background-color: #fff0f3;
    }
    h1, h2, h3 {
        color: #ff4d6d !important;
        text-align: center;
        font-family: 'Georgia', serif;
    }
    .letter-box {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        border-left: 5px solid #ff4d6d;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        color: #333;
        line-height: 1.6;
        font-size: 1.1rem;
        text-align: justify;
        max-height: 400px;
        overflow-y: auto;
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

    /* Envelope Styles */
    .envelope-container {
        position: relative;
        width: 250px;
        height: 180px;
        background: #ff4d6d;
        margin: 50px auto;
        border-radius: 0 0 10px 10px;
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
        color: #ff4d6d;
        border-radius: 5px;
    }

    /* Button Styling */
    .stButton>button {
        display: block;
        margin: 0 auto;
        border-radius: 30px;
        background-color: #ff4d6d;
        color: white;
        border: none;
        padding: 10px 40px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUNCTIONS ---
def play_audio():
    try:
        with open("ademi.mp3", "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            st.markdown(f'<audio autoplay loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>', unsafe_allow_html=True)
    except:
        pass

def spawn_emojis(emoji_type="❤️"):
    for i in range(12):
        pos = i * 8
        delay = i * 0.5
        st.markdown(f'<div class="emoji" style="left:{pos}vw; animation-delay:{delay}s;">{emoji_type}</div>', unsafe_allow_html=True)

# --- NAVIGATION ---
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# --- PAGES ---

if st.session_state.page == 'welcome':
    st.write("# Welcome Ade mii")
    spawn_emojis("❤️")
    if st.button("Next"):
        st.session_state.page = 'guess'
        st.rerun()

elif st.session_state.page == 'guess':
    play_audio()
    st.write("## A letter from yours truly...")
    st.write("### Guess who?")
    name = st.text_input("Input name:", key="name_box").lower().strip()
    
    if st.button("Submit"):
        valid = ["adenroye", "kanyinsola", "tamilore", "mistura", "baby", "babe"]
        if name in valid:
            st.session_state.page = 'success'
        else:
            st.session_state.page = 'wrong'
        st.rerun()

elif st.session_state.page == 'wrong':
    st.write("# Really? 💔")
    spawn_emojis("💔")
    if st.button("Try Again"):
        st.session_state.page = 'guess'
        st.rerun()

elif st.session_state.page == 'success':
    st.write("# That is why I love you!")
    st.markdown('<div class="envelope-container"><div class="envelope-flap"></div><div class="letter-paper">Open Me ✉️</div></div>', unsafe_allow_html=True)
    if st.button("Open"):
        st.session_state.page = 'letter_page'
        st.rerun()

elif st.session_state.page == 'letter_page':
    st.write("## For Adekunle Mi")
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
    if st.button("Next"):
        st.session_state.page = 'final'
        st.rerun()

elif st.session_state.page == 'final':
    st.write("# I love you Ade")
    spawn_emojis("💖")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Restart"):
            st.session_state.page = 'welcome'
            st.rerun()
    with c2:
        if st.button("Quit"):
            st.write("### Always and Forever. ❤️")
            st.stop()
