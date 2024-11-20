import streamlit as st
import random

# Title and subtitle with emojis for fun
st.markdown("<h1 style='text-align: center; color: crimson;'>💖 Love Life Calculator 💖</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: darkviolet;'>Find out your compatibility score with some fun preferences!</h3>", unsafe_allow_html=True)

# Sidebar for partner names input
st.sidebar.markdown("<h2 style='color: indigo;'>Enter Partner Details</h2>", unsafe_allow_html=True)

# Getting user input for partner names
partner1 = st.sidebar.text_input("Enter the first partner's name:")
partner2 = st.sidebar.text_input("Enter the second partner's name:")

# Preferences input
st.sidebar.markdown("<h3 style='color: darkorange;'>Choose Your Favorite!</h3>", unsafe_allow_html=True)
options = ["Beach 🏖️", "Mountain 🏔️", "Sun ☀️", "Rain 🌧️", "Snow ❄️"]
preference1 = st.sidebar.selectbox(f"What does {partner1} like?", options, key="p1")
preference2 = st.sidebar.selectbox(f"What does {partner2} like?", options, key="p2")

# Button to calculate the compatibility score
if st.sidebar.button("Calculate Love Score 💕"):
    if partner1.strip() and partner2.strip():  # Ensure names are not empty
        # Compatibility logic based on preferences
        compatibility_boost = 10 if preference1 == preference2 else 0
        base_love_score = random.randint(50, 90)
        love_score = base_love_score + compatibility_boost

        # Display compatibility result
        st.markdown(
            f"""
            <h2 style='text-align: center; color: hotpink;'>💘 {partner1} & {partner2}'s Love Score 💘</h2>
            <h1 style='text-align: center; color: limegreen;'>{love_score}%</h1>
            <p style='text-align: center; font-size: 18px; color: goldenrod;'> 
            {partner1} loves {preference1} and {partner2} loves {preference2}. 
            {'Great match! ❤️' if compatibility_boost else 'Opposites attract! 💕'}
            </p>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown("<h2 style='text-align: center; color: red;'>❗ Please enter both names and preferences to calculate the score.</h2>", unsafe_allow_html=True)

# Add a fun footer
st.markdown("<h4 style='text-align: center; color: gray;'>Made with 💖 by the Love Calculator Team</h4>", unsafe_allow_html=True)





