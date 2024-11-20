import streamlit as st
import random

# Title and subtitle with emojis for fun
st.markdown("<h1 style='text-align: center; color: crimson;'>💖 Love Life Calculator 💖</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: darkviolet;'>Find your compatibility score!</h3>", unsafe_allow_html=True)

# Sidebar for partner names input
st.sidebar.markdown("<h2 style='color: indigo;'>Enter Partner Names</h2>", unsafe_allow_html=True)

# Getting user input for partner names
partner1 = st.sidebar.text_input("Enter the first partner's name:")
partner2 = st.sidebar.text_input("Enter the second partner's name:")

# Button to calculate the compatibility score
if st.sidebar.button("Calculate Love Score 💕"):
    if partner1.strip() and partner2.strip():  # Ensure names are not empty
        # Generate a random love score between 50 and 100
        love_score = random.randint(50, 100)
        st.markdown(f"<h2 style='text-align: center; color: hotpink;'>💘 {partner1} & {partner2} are {love_score}% compatible! 💘</h2>", unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='text-align: center; color: red;'>❗ Please enter both names to calculate the score.</h2>", unsafe_allow_html=True)

