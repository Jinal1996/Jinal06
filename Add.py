import streamlit as st
import time
import random  # Ensure the random module is imported
import pandas as pd

# Inspirational quotes
quotes = [
    "“The mind is everything. What you think you become.” – Buddha",
    "“Peace comes from within. Do not seek it without.” – Buddha",
    "“Be happy in the moment, that's enough. Each moment is all we need, not more.” – Mother Teresa",
    "“The journey of a thousand miles begins with one step.” – Lao Tzu",
    "“Smile, breathe, and go slowly.” – Thich Nhat Hanh",
]

# Background music options
music_links = {
    "Nature Sounds 🌿": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    "Ocean Waves 🌊": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    "Relaxing Piano 🎹": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
}

# Mood options
moods = ["Happy 😊", "Calm 😌", "Stressed 😟", "Sad 😢", "Tired 😴", "Excited 🤩"]

# Title
st.markdown("<h1 style='text-align: center; color: darkblue;'>🧘‍♀️ Meditation Mood Tracker 🕰️</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: teal;'>Track how you feel before and after meditation.</h3>", unsafe_allow_html=True)

# Step 1: User's name and mood before meditation
st.sidebar.markdown("<h2 style='color: purple;'>Step 1: Enter Your Details</h2>", unsafe_allow_html=True)
user_name = st.sidebar.text_input("Enter your name:")
before_mood = st.sidebar.selectbox("How do you feel before meditation?", moods)

# Step 2: Meditation session
st.sidebar.markdown("<h2 style='color: purple;'>Step 2: Customize Your Session</h2>", unsafe_allow_html=True)
duration = st.sidebar.slider("Select meditation duration (minutes):", 1, 10, 5)
music = st.sidebar.selectbox("Choose background music:", list(music_links.keys()))

if st.sidebar.button("Start Meditation Timer 🕉️"):
    if user_name.strip():
        st.markdown(f"<h3 style='text-align: center; color: teal;'>Hello, {user_name}! Your meditation session starts now. 💖</h3>", unsafe_allow_html=True)
        with st.spinner("Relax and focus..."):
            for i in range(duration * 60, 0, -1):
                minutes, seconds = divmod(i, 60)
                st.markdown(f"<h2 style='text-align: center; color: green;'>Time Left: {minutes:02}:{seconds:02}</h2>", unsafe_allow_html=True)
                time.sleep(1)
                st.empty()

        # Inspirational quote
        quote = random.ch


