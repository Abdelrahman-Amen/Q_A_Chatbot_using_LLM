from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables from a .env file.

import streamlit as st  # Import Streamlit for creating the web application.
import os  # Import os for environment variable management.
import google.generativeai as genai  # Import Google's generative AI library.

# Configure the generative AI library using the API key from the environment variables.
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini Pro generative AI model and set up a chat session.
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])  # Start a chat session with an empty history.

# Function to send a question to the Gemini Pro model and retrieve the response.
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)  # Send the question and stream the response.
    return response  # Return the response object.

# Initialize the Streamlit app with a page title.
st.set_page_config(page_title="Q&A ChatBot")

# Add a header to the app.
st.header("Gemini LLM Application")

# Initialize session state to maintain chat history if it doesn't already exist.
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []  # Create an empty list for chat history.

# Create a text input field for user queries.
input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")  # Create a button to submit the query.

# When the user submits a query.
if submit and input:
    response = get_gemini_response(input)  # Get the AI response to the user query.
    # Add the user's query to the chat history.
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")  # Add a subheader for the AI's response.
    
    # Stream and display the response in chunks for real-time feedback.
    for chunk in response:
        st.write(chunk.text)  # Display each chunk of the AI's response.
        # Add the AI's response to the chat history.
        st.session_state['chat_history'].append(("Bot", chunk.text))

# Add a subheader for the chat history section.
st.subheader("The Chat History is")

# Display the chat history, showing both user inputs and AI responses.
for role, output_text in st.session_state['chat_history']:
    st.write(f"{role}: {output_text}")  # Display each message with its role.




    
