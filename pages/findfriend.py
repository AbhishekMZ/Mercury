import streamlit as st
import friend_recommendations

def find_friend():
    page = st.session_state.page
    # Set the title of the page
    st.title("Personality Test")

    # Define the questions and options
    questions = [
        {"question": "When working on a project, I prefer to", "options": ["Collaborate with others and bounce ideas off them", "Work independently and focus on my own thoughts"]},
        {"question": "In social situations, I tend to", "options": ["Thrive on being around people and engaging in conversations", "Feel drained or overwhelmed by too much social interaction"]},
        {"question": "When faced with a problem I usually", "options": ["Seek input and feedback from others", "Reflect on my own thoughts and ideas before seeking input"]},
        {"question": "When making decisions, I rely more on", "options": ["Concrete facts and data", "Patterns, possibilities, and my intuition"]},
        {"question": "In conversation, I tend to focus on", "options": ["Specific details and practical applications", "Theoretical concepts and exploring new ideas"]},
        {"question": "When planning for the future, I", "options": ["Break down tasks into discrete steps", "Envision the big picture and explore possibilities"]},
        {"question": "When evaluating a situation, I consider", "options": ["Logical analysis and objective criteria", "Personal values and the impact on people involved"]},
        {"question": "In conflicts, I tend to", "options": ["Focus on finding a fair and logical solution", "Consider the emotional well-being of those involved"]},
        {"question": "In my daily routine, I prefer", "options": ["A structured schedule and clear plans", "Flexibility and adapting to changing circumstances"]},
        {"question": "When faced with a deadline, I", "options": ["Create a plan and stick to it", "Take things as they come and adjust accordingly"]},
        {"question": "In social situations, I tend to", "options": ["Take charge and lead the conversation", "Go with the flow and see where the conversation takes us"]},
    ]

    # Create a form for the questionnaire
    with st.form("personality_test"):
        answers = []
        for i, q in enumerate(questions):
            st.markdown(f"<h3>{i+1}. {q['question']}</h3>", unsafe_allow_html=True)
            st.write(q['options'][0])
            answer = st.slider(f"slider_{i}", 1, 7,label_visibility="hidden")
            st.write(q['options'][1])
            answers.append(answer)
            st.write("\n\n\n")  # Add 3 empty lines for extra spacing
        submit_button = st.form_submit_button("Submit")

    # Process the answers when the form is submitted
    if submit_button:
        # You can add your logic here to process the answers
        st.write("Thank you for completing the personality test!")
        st.write("Your answers are:")
        for i, answer in enumerate(answers):
            st.write(f"{i+1}. {answer}")
        if page == "friend_recommendations.py":
            if hasattr(friend_recommendations, 'mentor_recommendations'):
                friend_recommendations.display_top_matches()
            else:
                st.error("Function 'find_friend' not found in 'find_friend' module.")
            if st.button("Go Back"):
                st.session_state.page = "menu_sel"  

find_friend()