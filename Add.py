import streamlit as st
import time
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

        # Step 3: Mood after meditation
        st.markdown("<h3 style='text-align: center; color: coral;'>How do you feel after meditation?</h3>", unsafe_allow_html=True)
        after_mood = st.selectbox("Select your mood after meditation:", moods, key="after_mood")

        # Submit results
        if st.button("Submit Mood Data"):
            st.markdown(f"<h3 style='text-align: center; color: darkgreen;'>Thank you, {user_name}!</h3>", unsafe_allow_html=True)

            # Analyze mood change
            if before_mood == after_mood:
                insight = "Your mood remained stable. Keep meditating for consistent peace. ✨"
            elif moods.index(after_mood) > moods.index(before_mood):
                insight = "Your mood improved after meditation! Keep it up! 🌟"
            else:
                insight = "Meditation can sometimes highlight feelings. Stay consistent for long-term benefits. 💖"

            st.markdown(f"<h4 style='text-align: center; color: royalblue;'>{insight}</h4>", unsafe_allow_html=True)

            # Store session data
            session_data = pd.DataFrame({
                "Name": [user_name],
                "Before Mood": [before_mood],
                "After Mood": [after_mood],
                "Duration (minutes)": [duration],
                "Music": [music],
            })
            st.markdown("<h3 style='text-align: center;'>Your Session Data:</h3>", unsafe_allow_html=True)
            st.dataframe(session_data)

            # Download session data
            csv = session_data.to_csv(index=False)
            st.download_button("Download Session Data", csv, "meditation_session.csv", "text/csv")
    else:
        st.markdown("<h3 style='text-align: center; color: red;'>Please enter your name to begin.</h3>", unsafe_allow_html=True)

# Footer
st.markdown("<h4 style='text-align: center; color: gray;'>💡 Keep meditating and tracking your progress!</h4>", unsafe_allow_html=True)

