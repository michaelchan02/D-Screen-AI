import streamlit as st
import requests

# Set your OpenAI API key
api_key = "KEY_HERE"

def generate_reminder(addiction_level, age, gender):
    try:
        prompt = f"Write a motivational and supportive reminder to help someone reduce their social media addiction. Take into account their addiction level: {addiction_level}, age: {age}, and gender: {gender}."

        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}",
            },
            json={
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "You are a friendly assistant."},
                    {"role": "user", "content": prompt}
                ]
            }
        ).json()

        print("OpenAI Response (Reminder):", response)  # Debugging line

        if 'choices' in response:
            return response['choices'][0]['message']['content']
        else:
            return f"An error occurred while generating the reminder: {response}"
    except Exception as e:
        print("Error:", e)
        return f"An error occurred while generating the reminder: {e}"

def generate_goal_conversation(addiction_level, interests, age, gender):
    try:
        prompt = f"Start a conversation to set goals and strategies for reducing social media usage. Take into account addiction level: {addiction_level}, interests: {interests}, age: {age}, and gender: {gender}."

        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}",
            },
            json={
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "You are a friendly assistant."},
                    {"role": "user", "content": prompt}
                ]
            }
        ).json()

        print("OpenAI Response (Goal Conversation):", response)  # Debugging line

        if 'choices' in response:
            return response['choices'][0]['message']['content']
        else:
            return f"An error occurred while generating the goal-setting conversation: {response}"
    except Exception as e:
        print("Error:", e)
        return f"An error occurred while generating the goal-setting conversation: {e}"

# Function to map slider values to addiction levels
def map_addiction_level(value):
    levels = {1: "Mild", 5: "Moderate", 10: "Strong"}
    return levels.get(value, str(value))

# Streamlit App
st.title("Social Media Limitation Assistant")

addiction_level = st.slider(
    "How strong is your social media addiction?",
    min_value=1,
    max_value=10,
    step=1,
    value=5
)

age = st.number_input("What is your age?", min_value=0, max_value=150, step=1, value=18)

gender = st.radio("What is your gender?", ("Male", "Female", "Other"))

interests = st.text_input("What are your hobbies or interests?")

if st.button("Generate Reminder"):
    reminder = generate_reminder(map_addiction_level(addiction_level), age, gender)
    st.write("Reminder:")
    st.write(reminder)

if st.button("Start Goal Setting Conversation"):
    goal_conversation = generate_goal_conversation(map_addiction_level(addiction_level), interests, age, gender)
    st.write("Goal Setting Conversation:")
    st.write(goal_conversation)
