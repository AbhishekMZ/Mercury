import streamlit as st
import findfriend
import mentor

def menu_sel():
    # Set default page to "main" if not in session state
    if "page" not in st.session_state:
        st.session_state.page = "main"
    page = st.session_state.page

    if page == "main":
        st.title("How would you like to proceed?")

        # Two large buttons
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Find a Friend", key="find_friend", use_container_width=True):
                st.session_state.page = "find_friend"
        st.write("Connect with someone who shares similar interests and hobbies.")

        with col2:
            if st.button("Meet a Mentor", key="meet_mentor", use_container_width=True):
                st.session_state.page = "mentor"
        st.write("Get guidance and advice from someone with experience and expertise.")

    elif page == "find_friend":
        if hasattr(findfriend, 'find_friend'):
            findfriend.find_friend()
        else:
            st.error("Function 'find_friend' not found in 'find_friend' module.")
        if st.button("Go Back"):
            st.session_state.page = "main"

    elif page == "mentor":
        if hasattr(mentor, 'find_student_mentor'):
            mentor.find_student_mentor()
        else:
            st.error("Function 'find_student_mentor' not found in 'mentor' module.")
        if st.button("Go Back"):
            st.session_state.page = "main"

menu_sel()
