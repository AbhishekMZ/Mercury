
import streamlit as st
import mentor_recommendations

def find_student_mentor():
    st.title("Help us understand the qualities you look for in a student mentor!")
    page = st.session_state.page
    # Question 1
    st.write("What is the most important trait you look for in a mentor? (Select up to 2)")
    traits = st.multiselect("", [
        "Practical skills",
        "Strong communication skills",
        "Similar career goals or background",
        "Emotional intelligence",
        "Sense of humor"
    ])

    st.write("")  # Add a blank line between questions

    # Question 2
    st.write("How often would you like to communicate with your mentor?")
    communication_frequency = st.radio("", ["Rarely", "Sometimes", "Often"], index=None)

    st.write("")  # Add a blank line between questions

    # Question 3
    st.write("What kind of guidance do you seek?")
    guidance_type = st.radio("", [
        "Career advice",
        "Industry insights & networking opportunities",
        "Skill development",
        "Personal growth and development"
    ], index=None)

    st.write("")  # Add a blank line between questions

    # Question 4
    st.write("How would you like your mentor to provide feedback?")
    feedback_type = st.radio("", [
        "Constructive criticism",
        "Encouragement and support",
        "Regular check-ins",
        "Goal-setting and accountability"
    ], index=None)

    st.write("")  # Add a blank line between questions

    # Question 5
    st.write("Would you prefer a mentor who is")
    mentor_background = st.radio("", [
        "From a similar cultural background",
        "From a different cultural background",
        "The same gender as you",
        "No preference"
    ], index=None)

    st.write("")  # Add a blank line between questions

    # Question 6
    st.write("Are there any specific industries or sectors you're interested in being mentored in? (Select up to 2)")
    industries = st.multiselect("", [
        "Technology",
        "Healthcare",
        "Finance",
        "Education",
        "Arts and Design"
    ])

    st.write("")  # Add a blank line between questions

    # Question 7
    st.write("Are there any particular skills or areas you'd like to develop with the help of a mentor? (Select up to 2)")
    skills = st.multiselect("", [
        "Leadership",
        "Communication",
        "Time management",
        "Public speaking",
        "Networking"
    ])

    # Submit button
    submit_button = st.button("Submit")
    if submit_button:
        st.write("Your input:")
        st.write("Traits:", traits)
        st.write("Communication frequency:", communication_frequency)
        st.write("Guidance type:", guidance_type)
        st.write("Feedback type:", feedback_type)
        st.write("Mentor background:", mentor_background)
        st.write("Industries:", industries)
        st.write("Skills:", skills)
        
        if page == "mentor_recommendations.py":
            if hasattr(mentor_recommendations, 'mentor_recommendations'):
                mentor_recommendations.display_top_matches()
            else:
                st.error("Function 'find_friend' not found in 'find_friend' module.")
            if st.button("Go Back"):
                st.session_state.page = "menu_sel"   

find_student_mentor()