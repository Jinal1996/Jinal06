import streamlit as st
import random

# Title and subtitle
st.markdown("<h1 style='text-align: center; color: crimson;'>💖 Love Life Calculator 💖</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: darkviolet;'>Find your compatibility score with fun preferences!</h3>", unsafe_allow_html=True)

# Sidebar for partner names input
st.sidebar.markdown("<h2 style='color: indigo;'>Enter Partner Details</h2>", unsafe_allow_html=True)

# Input names of the two partners
partner1 = st.sidebar.text_input("Enter the first partner's name:")
partner2 = st.sidebar.text_input("Enter the second partner's name:")

# Sidebar for preferences
st.sidebar.markdown("<h3 style='color: darkorange;'>Choose Preferences</h3>", unsafe_allow_html=True)

# Preference categories
categories = {
    "Place": ["Beach 🏖️", "Mountain 🏔️", "City 🏙️", "Countryside 🌾"],
    "Food": ["Italian 🍝", "Indian 🍛", "Chinese 🥡", "Mexican 🌮"],
    "Clothes": ["Casual 👕", "Formal 👔", "Traditional 🥻", "Trendy 👗"],
    "Music": ["Pop 🎵", "Classical 🎻", "Rock 🎸", "Jazz 🎷"],
    "Hobby": ["Reading 📚", "Traveling ✈️", "Sports ⚽", "Dance 💃"],
}

# Collect preferences for both partners
preferences1 = {}
preferences2 = {}

for category, options in categories.items():
    preferences1[category] = st.sidebar.selectbox(f"{partner1}'s favorite {category}:", options, key=f"{category}_p1")
    preferences2[category] = st.sidebar.selectbox(f"{partner2}'s favorite {category}:", options, key=f"{category}_p2")

# Button to calculate the compatibility score
if st.sidebar.button("Calculate Love Score 💕"):
    if partner1.strip() and partner2.strip():
        # Calculate compatibility based on matching preferences
        matches = sum(preferences1[category] == preferences2[category] for category in categories)
        base_love_score = random.randint(50, 70)
        love_score = base_love_score + matches * 5  # Add 5% for each matching preference
        
        # Display compatibility results
        st.markdown(
            f"""
            <h2 style='text-align: center; color: hotpink;'>💘 {partner1} & {partner2}'s Love Score 💘</h2>
            <h1 style='text-align: center; color: limegreen;'>{love_score}%</h1>
            <p style='text-align: center; font-size: 18px; color: goldenrod;'> 
            {matches} out of {len(categories)} preferences matched! 
            {'A match made in heaven! ❤️' if matches > len(categories) // 2 else 'Opposites attract! 💕'}
            </p>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown("<h2 style='text-align: center; color: red;'>❗ Please enter both names and all preferences to calculate the score.</h2>", unsafe_allow_html=True)

# Footer
st.markdown("<h4 style='text-align: center; color: gray;'>Made with 💖 for fun!</h4>", unsafe_allow_html=True)



