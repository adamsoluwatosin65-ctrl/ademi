<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600&family=Quicksand:wght@300;500&display=swap');

/* Custom Heart Cursor */
html, body, * {
    cursor: url('https://cdn-icons-png.flaticon.com/32/2107/2107845.png'), auto !important;
}

/* Luxury Glassmorphism Letter Box */
.letter-box {
    background: rgba(255, 255, 255, 0.15) !important;
    backdrop-filter: blur(15px) !important;
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
    padding: 40px;
    border-radius: 30px;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2);
    color: #4a0000 !important;
    line-height: 2;
    font-size: 1.25rem;
}

/* Moving Soft Gradient */
.stApp {
    background: linear-gradient(135deg, #fce4ec 0%, #ffe0b2 50%, #f8bbd0 100%);
    background-size: 200% 200%;
    animation: flow 10s ease infinite;
}

@keyframes flow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Polished Buttons */
.stButton>button {
    background: rgba(211, 47, 47, 0.8) !important;
    backdrop-filter: blur(5px);
    border: 1px solid rgba(255, 255, 255, 0.4) !important;
    letter-spacing: 2px;
    text-transform: uppercase;
    transition: 0.5s !important;
}

.stButton>button:hover {
    letter-spacing: 5px;
    background: #d32f2f !important;
    box-shadow: 0 0 20px rgba(211, 47, 47, 0.6);
}
</style>
