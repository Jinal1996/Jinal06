import streamlit as st
import random

# Vacation data: Pre-defined destinations with categories
destinations = [
    {
        "name": "Maldives",
        "category": "Beach",
        "weather": "Warm",
        "budget": "High",
        "image": "https://www.tourism.gov.mv/images/hero.jpg",
        "description": "Crystal-clear waters, white sandy beaches, and luxury resorts await you in the Maldives! 🏝️",
    },
    {
        "name": "Swiss Alps",
        "category": "Mountains",
        "weather": "Cold",
        "budget": "High",
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/88/Swiss_Alps_%28pixinn.net%29.jpg",
        "description": "Experience breathtaking views, skiing, and cozy chalets in the Swiss Alps! 🏔️",
    },
    {
        "name": "Tokyo",
        "category": "City",
        "weather": "Mild",
        "budget": "Medium",
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/0c/Tokyo_Skyline.jpg",
        "description": "Dive into the bustling energy of Tokyo, with neon lights, culture, and sushi! 🏙️",
    },
    {
        "name": "Bali",
        "category": "Beach",
        "weather": "Warm",
        "budget": "Medium",
        "image": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Bali_Hindu_temple.jpg",
        "description": "Relax at beautiful beaches, explore temples, and enjoy tropical vibes in Bali! 🌴",
    },
    {
        "name": "Banff",
        "category": "Mountains",
        "weather": "Cold",
        "budget": "Medium",
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/1e/Banff_Lake.jpg",
        "description": "Discover turquoise lakes and rugged peaks in Banff National Park! ❄️",
    },
]

# Title and subtitle
st.markdown(
    "<h1 style='text-align: center; color: darkblue;'>🌍 Dream Vacation Generator 🧳</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h3 style='text-align: center; color: teal;'>Select your preferences and find your perfect getaway!</h3>",
    unsafe_allow_html=True,
)

# Sidebar for preferences
st.sidebar.markdown("<h2 style='color: purple;'>Your Preferences</h2>", unsafe_allow_html=True)

# Dropdown for preferences
category = st.sidebar.selectbox("What type of place do you like?", ["Beach", "Mountains", "City"])
weather = st.sidebar.selectbox("Preferred weather?", ["Warm", "Cold", "Mild"])
budget = st.sidebar.selectbox("Your budget?", ["High", "Medium"])

# Button to generate a vacation
if st.sidebar.button("Find My Vacation! ✈️"):
    # Filter destinations based on preferences
    filtered_destinations = [
        d for d in destinations if d["category"] == category and d["weather"] == weather and d["budget"] == budget
    ]

    if filtered_destinations:
        # Randomly select a destination
        vacation = random.choice(filtered_destinations)
        st.markdown(
            f"""
            <h2 style='text-align: center; color: gold;'>✨ Your Dream Vacation: {vacation['name']} ✨</h2>
            <p style='text-align: center; color: darkgreen;'>{vacation['description']}</p>
            <img src="{vacation['image']}" style='display: block; margin: 0 auto; width: 80%; border-radius: 10px;'>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            "<h2 style='text-align: center; color: red;'>Sorry! No destinations match your preferences. Try changing your options. 🙁</h2>",
            unsafe_allow_html=True,
        )

# Footer
st.markdown(
    "<h4 style='text-align: center; color: gray;'>💡 Made with Streamlit for your next adventure!</h4>",
    unsafe_allow_html=True,
)


