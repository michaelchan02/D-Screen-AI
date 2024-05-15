import streamlit as st
import pandas as pd
from openai import OpenAI
time_management_tips = pd.read_csv("time_management_tips.csv")

# Setup OpenAI client
client = OpenAI(api_key="my-api-key")

time_management_tips = pd.read_csv("time_management_tips.csv")

# Streamlit page configuration
st.set_page_config(page_title="Time Management Chatbot", layout="wide")

# Introduction text
st.title("Time Management Chatbot")
st.write("Hello! I'm a chatbot here to help you improve your time management skills.")
st.write("Please tell me what you're struggling with or what you'd like to improve:")
st.write("Here’s a random time management tip for you:")
random_tip = time_management_tips.sample().iloc[0]
st.write(f"**Tip**: {random_tip['Tip']}")
st.write(f"**Description**: {random_tip['Description']}")

# Input from user
user_query = st.text_input("Enter your question about time management or type 'exit' to end:")

if user_query:
    # Check if user wants to exit
    if user_query.lower() == 'exit':
        st.write("Thank you for visiting. Feel free to come back anytime!")
    else:
        # Manage initial flag with session state
        if 'initial' not in st.session_state:
            st.session_state.initial = True

        # Create the prompt based on the user's input
        if st.session_state.initial:
            prompt = f"Given a student's question about time management: '{user_query}', provide detailed advice on improving time management skills."
            st.session_state.initial = False
        else:
            prompt = user_query

        # Get response from OpenAI's model
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            temperature=0.7,
            max_tokens=200,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        # Display the response
        st.write(response.choices[0].text.strip())
        st.write("Ask me further questions or type 'exit' to stop.")
