import streamlit as st
import time
import random
import pandas as pd

# Inspirational quotes
quotes = [
    "“The mind is everything. What you think you become.” – Buddha",
    "“Peace comes from within. Do not seek it without.” – Buddha",
    "“Be happy in the moment, that's enough. Each moment is all we need, not more.” – Mother Teresa",
    "“The journey of a thousand miles begins with one step.” – Lao Tzu",
    "“Smile, breathe, and go slowly.” – Thich Nhat Hanh",
]

# Mood suggestions
suggestions = {
    "Happy 😊": "Keep doing what you're doing! Share your joy with someone.",
    "Stressed 😟": "Try deep breathing or a short walk. Relax your shoulders.",
    "Sad 😢": "Listen to uplifting music or call a loved one.",
    "Tired 😴": "Take a power nap or have a cup of tea.",
    "Excited 🤩": "Channel your energy into something creative!",
}

# Background music options
music_links = {
    "Nature Sounds 🌿": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    "Ocean Waves 🌊": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    "Relaxing Piano 🎹": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
}

# Title and subtitle
st.markdown(
    "<h1 style='text-align: center; color: darkblue;'>🧘‍♀️ Mindfulness & Mental Health Tracker 🕰️</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h3 style='text-align: center; color: teal;'>Track your mood and focus on your well-being.</h3>",
    unsafe_allow_html=True,
)

# Collect user name
user_name = st.text_input("Enter your name to personalize your session:")

# Sidebar for tracking
st.sidebar.markdown("<h2 style='color: purple;'>Customize Your Session</h2>", unsafe_allow_html=True)
mood = st.sidebar.selectbox("How are you feeling today?", list(suggestions.keys()))
duration = st.sidebar.slider("Select mindfulness duration (minutes):", 1, 10, 5)
music = st.sidebar.selectbox("Choose background music:", list(music_links.keys()))

# Start mindfulness session
if st.sidebar.button("Start Mindfulness Timer 🕉️"):
    if user_name.strip():
        # Show a soothing animation
        st.markdown(f"<h3 style='text-align: center; color: teal;'>Hello, {user_name}! Your session starts now. 💖</h3>", unsafe_allow_html=True)
        with st.spinner("Relax and focus..."):
            for i in range(duration * 60, 0, -1):
                minutes, seconds = divmod(i, 60)
                st.markdown(
                    f"<h2 style='text-align: center; color: green;'>Time Left: {minutes:02}:{seconds:02}</h2>",
                    unsafe_allow_html=True,
                )
                time.sleep(1)
                st.empty()  # Clear the previous timer text

        # Inspirational quote
        quote = random.choice(quotes)
        st.markdown(
            f"""
            <h2 style='text-align: center; color: gold;'>✨ Session Complete! ✨</h2>
            <p style='text-align: center; color: darkgreen; font-size: 20px;'>{quote}</p>
            """,
            unsafe_allow_html=True,
        )
        # Embed background music
        st.markdown(
            f"""
            <audio controls autoplay>
              <source src="{music_links[music]}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
            """,
            unsafe_allow_html=True,
        )

        # Display mood suggestions
        st.markdown(
            f"<h3 style='text-align: center; color: coral;'>Mood Suggestion:</h3><p style='text-align: center;'>{suggestions[mood]}</p>",
            unsafe_allow_html=True,
        )

        # Save session data
        session_data = pd.DataFrame({
            "Name": [user_name],
            "Mood": [mood],
            "Duration (minutes)": [duration],
            "Music": [music],
        })
        st.markdown("<h3 style='text-align: center;'>Your Session Data:</h3>", unsafe_allow_html=True)
        st.dataframe(session_data)

        # Option to download session data
        csv = session_data.to_csv(index=False)
        st.download_button("Download Session Data", csv, "session_data.csv", "text/csv")
    else:
        st.markdown("<h3 style='text-align: center; color: red;'>Please enter your name to begin.</h3>", unsafe_allow_html=True)

# Footer
st.markdown(
    "<h4 style='text-align: center; color: gray;'>💡 Take care of your mind, body, and soul!</h4>",
    unsafe_allow_html=True,
)

