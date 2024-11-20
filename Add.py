import streamlit as st
import random
import pyperclip  # For copying to clipboard

# Local database of jokes
jokes = [
    "Why don’t skeletons fight each other? Because they don’t have the guts. 😂",
    "Why did the scarecrow win an award? Because he was outstanding in his field. 🌾",
    "What do you call fake spaghetti? An impasta. 🍝",
    "I told my wife she was drawing her eyebrows too high. She looked surprised. 😲",
    "Why don’t eggs tell jokes? They’d crack each other up. 🥚",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one. 🏌️‍♂️",
]

# Title and subtitle
st.markdown(
    "<h1 style='text-align: center; color: purple;'>😂 Joke Generator 🎉</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h3 style='text-align: center; color: darkblue;'>Click the button below to brighten your day!</h3>",
    unsafe_allow_html=True,
)

# Button to generate a joke
if st.button("Get a Joke! 🎈"):
    # Randomly select a joke
    joke = random.choice(jokes)
    st.markdown(
        f"""
        <h2 style='text-align: center; color: darkgreen;'>Here's your joke:</h2>
        <p style='text-align: center; font-size: 20px; color: teal;'>{joke}</p>
        """,
        unsafe_allow_html=True,
    )

    # Copy to clipboard button
    if st.button("Copy Joke to Clipboard ✂️"):
        pyperclip.copy(joke)
        st.success("Joke copied to




