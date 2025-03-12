
import streamlit as st # for the web interface
import random # for randomizing the questions
import time # for the timer

# Title of the Application
st.title("📝 Quiz Application")

# Define quiz questions, options, and answer in the form of a list of dictionaries
questions = [
    {
        "question": "which lauguage is dynamically typed?",
        "options": ["java", "Python", "Both", "None"],
        "answer": "Python",
    },
    {
        "question": "which lauguage is faster in execution ?",
        "options": ["Java", "Python", "Both", "None"],
        "answer": "Java",
    },
    {
        "question": "which lauguage is mainly used for Andriod development?",
        "options": ["Python", "Java", "C++", "JavaScript"],
        "answer": "Java",
    },
    {
        "question": "Which lauguage is uses identation for code blocks?",
        "options": ["Java", "Python", "C", "Ruby"],
        "answer": "Python",
    },
    {
        "question": "Which lauguage is best for AI and Machine learning?",
        "options": ["JavaScript", "Python", "PHP", "Ruby"],
        "answer": "Python",
    },
    {
        "question": "which lauguage  requires  explicit type declaration?",
        "options": ["Ruby", "Java", "SQl", "JavaScript"],
        "answer" : "Java"
    },  
]

# Initialize a random question if none exists in the session state
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

# Get the current question from session state
question = st.session_state.current_question

# Display the question
st.subheader(question["question"])

# Create radio buttons for the options
selected_option = st.radio("Choose your answer", question["options"], key="answer")

# Submit button the check the answer
if st.button("Submit Answer"):
    # check if the answer is correct
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
    else:
        st.error("❌ Incorrect! the correct answer is " + question["answer"])
  
    # Wait for 3 seconds before showing the next question
    time.sleep(5)

    # Select a new random question
    st.session_state.current_question = random.choice(questions)

    # Rerun the app to display the next question    
    st.rerun()
