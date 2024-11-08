import streamlit as st
import random

# Title of the portfolio
st.title("My Portfolio")

# Introduction
st.header("Hi,I am DhivyaLaxmi")
st.write("A Data Analysis From Coimbatore")
st.write("I am graduated student in Anna University. AIDS department")
st.write("Intrested in tech")

# Contact Information
st.header("Contact Me:9150364411")
st.write("Feel free to reach out via email: [dhivyalaxmi2031@gmail.com]")

# Title and description
st.title("Guess The Number")
st.write("I will think of a number between 0 and 50. Try to guess the number within fewer attempts.")

# Initialize session state to keep track of the game state
if 'computer_guess' not in st.session_state:
    st.session_state.computer_guess = random.randint(0, 50)  # Random number between 0 and 50
    st.session_state.attempts = 0  # Track the number of attempts

# Function to handle the guessing logic
def guess():
    # User input
    user_guess = st.number_input("Enter your guess:", min_value=0, max_value=50, step=1)

    if user_guess:
        # Increment attempts count
        st.session_state.attempts += 1

        # Check the guess
        if user_guess < st.session_state.computer_guess:
            st.write("Guess higher!")
        elif user_guess > st.session_state.computer_guess:
            st.write("Guess lower!")
        else:
            st.success(f"Congratulations! You guessed the correct number {st.session_state.computer_guess} in {st.session_state.attempts} attempts.")
            # Reset the game
            if st.button("Play Again"):
                st.session_state.computer_guess = random.randint(0, 50)  # Generate a new number
                st.session_state.attempts = 0  # Reset attempts

# Run the guess function
guess()
