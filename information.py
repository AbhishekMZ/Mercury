import streamlit as st

def tell_us_about_yourself():
    st.title("Tell us about yourself!")

    name = st.text_input("Enter your name")

    gender_options = ["Male", "Female"]
    gender_placeholder = st.selectbox("Gender", ["Choose an option"] + gender_options)

    year_of_study_options = ["1st year", "2nd year", "3rd year", "4th year", "Post Graduate/PHD"]
    year_of_study_placeholder = st.selectbox("Year of Study", ["Choose an option"] + year_of_study_options)

    branch_options = [
        "Computer Science and Engineering",
        "Computer Science (Data Science)",
        "Computer Science (Cyber Security)",
        "Information Science and Engineering",
        "Artificial Intelligence & Machine Learning",
        "Electronics and Communication Engineering",
        "Electrical and Electronics Engineering",
        "Electronics and Telecommunication Engineering",
        "Electronics and Instrumentation Engineering",
        "Mechanical Engineering",
        "Biotechnology",
        "Aerospace Engineering",
        "Chemical Engineering",
        "Industrial Engineering and Management",
        "Civil Engineering"
    ]
    branch_placeholder = st.selectbox("Branch (only applicable to RVCE students)", ["Choose an option"] + branch_options)

    field_of_study_options = [
        "STEM- Science, Technology, Engineering, Mathematics",
        "Commerce/Management/Business",
        "Art/Literature/Humanities"
    ]
    field_of_study_placeholder = st.selectbox("Field of study", ["Choose an option"] + field_of_study_options)

    hobbies_options = [
        "Creative hobbies - Sketching/Writing/Photography",
        "Physical hobbies - Sports/Fitness/Gymming/Dancing",
        "Intellectual hobbies – Reading/Puzzles/Games",
        "Social hobbies – Volunteering/Baking/Event organizing",
        "Performing arts – Acting/Singing/Stand-up comedy"
    ]
    hobbies_placeholder = st.selectbox("What type of hobbies are you primarily into?", ["Choose an option"] + hobbies_options)

    languages_options = [
        "English",
        "Hindi",
        "Kannada",
        "Telugu",
        "Tamil"
    ]
    languages = st.multiselect("What's your preferred language for communication? (select all that apply)", languages_options)

    submit_button = st.button("Submit")
    if submit_button:
        st.write("Your input:")
        st.write("Name:", name)
        st.write("Gender:", gender_placeholder)
        st.write("Year of Study:", year_of_study_placeholder)
        st.write("Branch:", branch_placeholder)
        st.write("Field of study:", field_of_study_placeholder)
        st.write("Hobbies:", hobbies_placeholder)
        st.write("Preferred language for communication:", languages)

tell_us_about_yourself()

