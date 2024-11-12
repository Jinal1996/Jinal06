import streamlit as st

# Title and subtitle with emojis for added color
st.markdown("<h1 style='text-align: center; color: purple;'>🌈 Fun Adding App for Toddlers 🌈</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: teal;'>Let's add two numbers together!</h3>", unsafe_allow_html=True)

# Sidebar for user inputs
st.sidebar.markdown("<h2 style='color: darkblue;'>Enter Your Numbers</h2>", unsafe_allow_html=True)

# Getting user input for the first and second number
first_number = st.sidebar.number_input("Enter the first number:", min_value=0, step=1)
second_number = st.sidebar.number_input("Enter the second number:", min_value=0, step=1)

# Button to calculate the sum
if st.sidebar.button("Calculate Sum"):
    result = first_number + second_number
    # Display the result in a colorful message
    st.markdown(f"<h2 style='text-align: center; color: green;'>🎉 The sum is: {result} 🎉</h2>", unsafe_allow_html=True)
