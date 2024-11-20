import streamlit as st
import time
import random

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

# Title and subtitle
st.markdown(
    "<h1 style='text-align: center; color: darkblue;'>🧘‍♀️ Mindfulness Timer 🕰️</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h3 style='text-align: center; color: teal;'>Take a moment to relax and focus.</h3>",
    unsafe_allow_html=True,
)

# Sidebar for timer duration and music
st.sidebar.markdown("<h2 style='color: purple;'>Customize Your Session</h2>", unsafe_allow_html=True)
duration = st.sidebar.slider("Select duration (minutes):", 1, 10, 5)
music = st.sidebar.selectbox("Choose background music:", list(music_links.keys()))

# Button to start the timer
if st.sidebar.button("Start Mindfulness Timer 🕉️"):
    # Show a soothing animation
    with st.spinner("Relax and focus..."):
        for i in range(duration * 60, 0, -1):
            minutes, seconds = divmod(i, 60)
            st.markdown(
                f"<h2 style='text-align: center; color: green;'>Time Left: {minutes:02}:{seconds:02}</h2>",
                unsafe_allow_html=True,
            )
            time.sleep(1)
            st.empty()  # Clear the previous timer text

    # Display an inspirational quote after the timer
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

# Footer
st.markdown(
    "<h4 style='text-align: center; color: gray;'>💡 Relax, refresh, and come back stronger!</h4>",
    unsafe_allow_html=True,
)



