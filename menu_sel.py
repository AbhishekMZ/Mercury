import streamlit as st
import findfriend
import meetmentor

def menu_sel():
    page = st.session_state.get("page", "main")

    if page == "main":
        st.title("How would you like to proceed?")

        # Two large buttons
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Find a Friend", key="find_friend", type="primary", use_container_width=True):
                st.session_state.page = "find_friend"
            st.write("Connect with someone who shares similar interests and hobbies.")

        with col2:
            if st.button("Meet a Mentor", key="meet_mentor", type="primary", use_container_width=True):
                st.session_state.page = "meet_mentor"
            st.write("Get guidance and advice from someone with experience and expertise.")

    elif page == "find_friend":
        findfriend.main()

    elif page == "meet_mentor":
        meetmentor.main()


menu_sel()