import streamlit as st
import pandas as pd
import information

# Create a dataframe to store user data
user_data = pd.DataFrame(columns=['Name', 'Email', 'Password'])

# Function to register a new user
def register_user(name, email, password):
    new_user = pd.DataFrame({'Name': [name], 'Email': [email], 'Password': [password]})
    global user_data
    user_data = pd.concat([user_data, new_user], ignore_index=True)
    return "User registered successfully!"

# Function to sign in a user
def sign_in(email, password):
    # TO DO: implement sign in logic here
    return "Sign in successful!"

# Welcome page
st.title("Mercury")
st.write("Cultivating Meaningful Connections")

# Choice between sign in and register
choice = st.selectbox("What would you like to do?", ["Sign In", "Register"])

if choice == "Sign In":
    # Sign in page
    st.title("Sign In")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submit_button = st.button("Sign In")
    if submit_button:
        result = sign_in(email, password)
        st.success(result)
        st.session_state.page = "check_back_in"
        st.experimental_rerun()
elif choice == "Register":
    # Registration form
    st.title("Register")
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    submit_button = st.button("Register")
    if submit_button:
        if password == confirm_password:
            result = register_user(name, email, password)
            st.success(result)
            st.session_state.page = "information"
            st.rerun()  # Corrected line
        else:
            st.error("Passwords do not match. Please try again.")

# Check if the user should be redirected to another page
if "page" in st.session_state:
    if st.session_state.page == "check_back_in":
        st.title("Check back in with us")
        st.write("Welcome back!")
    elif st.session_state.page == "information":
        information.tell_us_about_yourself()

# Display user data
st.write("Registered Users:")
st.write(user_data)
