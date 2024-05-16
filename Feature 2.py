import streamlit as st 
from openai import OpenAI 

client = OpenAI(api_key="my-api-key") 

# Streamlit page configuration
st.set_page_config(page_title="📱Social Media Addiction Assessment", layout="centered")
st.title("📱Social Media Addiction Assessment")

# Define the URL of your logo image
header_image_url = "https://onecms-res.cloudinary.com/image/upload/s--__Kxlh52--/f_auto,q_auto/c_fill,g_auto,h_622,w_830/v1/mediacorp/tdy/image/2023/07/21/20230722-ns-dlbigread0722.jpg?itok=nR5234vF"  # Corrected image URL

# Display the logo image above the title
st.image(header_image_url, use_column_width=True)

# Define the Assessment Question
questions = [
        {"text": "1. How often do you find yourself mindlessly scrolling through social media without a specific purpose?", "type": "likert"}, 
        {"text": "2. Have you ever thought about reducing your social media usage, but found it difficult to do so?", "type": "likert"},
        {"text": "3. How do you feel when you don't have access to your social media accounts?", "type": "dropdown", "options":["Very Dissatisfied", "Dissatisfied", "Neither", "Satisfied", "Very Satisfied"]},
        {"text": "4. How often do you experience feelings of jealousy or inadequacy when comparing yourself to others on social media?", "type": "likert"},
        {"text": "5. Do you often check your social media accounts first thing in the morning and right before bed?", "type": "likert"},
        {"text": "6. Have you ever missed important tasks or events because you were too caught up in social media?", "type": "likert"},
        {"text": "7. Do you find yourself prioritizing social media over spending time with friends and family?", "type": "likert"},
        {"text": "8. How often do you have conflicts with loved ones because of your social media usage?", "type": "likert"},
        {"text": "9. How often do you procrastinate on important tasks because you were using social media?", "type": "likert"},
        {"text": "10. Do you find yourself spending more time on social media than working towards your personal or professional goals?", "type": "likert"},
        {"text": "11. Do you experience symptoms of anxiety or depression when you are unable to access social media?", "type": "likert"},
        {"text": "12. How often do you experience a decrease in your overall well-being since increasing your social media usage?", "type": "likert"},
        {"text": "13. Have you set limits for yourself on how much time you can spend on social media, and do you find it hard to stick to them?", "type": "likert"},
        {"text": "14. Do you often feel like your social media usage controls you?", "type": "likert"}
    ]

 # Likert_scale options
likert_scale = ["Very Rarely", "Rarely", "Sometimes", "Often", "Very Often"]
dropdown_scale = ["Very Satisfied", "Satisfied", "Neither", "Dissatisfied", "Very Dissatisfied"]

    # Function to collect user responses and calculate addiction score
def collect_responses():
        score = 0
        for i, question in enumerate(questions):
            if question["type"] == "likert":
                st.write(question["text"])
                likert_scale_options = ["Very Rarely", "Rarely", "Sometimes", "Often", "Very Often"]
                response = st.select_slider("", options=likert_scale_options, key=f"likert_{i}")
                # Calculate score based on response
                score += likert_scale_options.index(response) + 1
                st.markdown("<br><br>", unsafe_allow_html=True)           
            elif question["type"] == "dropdown":
                st.write(question["text"])
                dropdown_options = question["options"]
                option_scores = {option: idx + 1 for idx, option in enumerate(dropdown_options)}
                response = st.selectbox("", options=dropdown_options, key=f"dropdown_{i}")
                # Add score based on selected option
                score += option_scores[response]
                st.markdown("<br><br>", unsafe_allow_html=True)
        return score

    # Function to analyze responses and determine social media addiction score
def analyze_responses(responses):
        score = 0
        # Define mapping of Likert scale options to scores
        likert_scores = {
            "Very Rarely": 1,
            "Rarely": 2,
            "Sometimes": 3,
            "Often": 4,
            "Very Often": 5
        }
        # Analyze responses and calculate score
        for response in responses:
            if isinstance(response, str):
                # Handle dropdown responses
                score += response
            else:
                # Handle Likert scale responses
                score += response
        return score

    # Streamlit Intro Text
def main():
        st.write("Hello! This tool is designed to help you identify what level of social media addiction you have by asking you a series of questions.")
        st.markdown("<br><br>", unsafe_allow_html=True) 

        # Display questions and update addiction score dynamically
        addiction_score = collect_responses()
        
        # Determine addiction level based on score
        if 14 <= addiction_score <= 33:
            st.write("Congratulations! Your social media addiction level is low.")
        elif 34 <= addiction_score <= 51:
            st.write("Your social media addiction level is moderate. Consider setting boundaries.")
        elif addiction_score >= 52:
            st.write("Your social media addiction level is high. It may be time to seek help.")
        st.write(f"Your social media addiction score is: {addiction_score}")

    # Get response from OpenAi's model
        prompt = "Write a response based on the user's social media addiction score."
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            temperature=0.7,
            max_tokens=400,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        st.write(response.choices[0].text.strip())

main()
