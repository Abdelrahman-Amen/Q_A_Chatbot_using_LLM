# Q&A Chatbot

# What is LLM? 🔮

LLM (Large Language Model) refers to advanced AI models trained on vast text data to understand and generate human-like language. These models, like Google Gemini or GPT, can:

• 📝 Generate content.

• ❓ Answer questions.

• 🌐 Translate languages.

• 📖 Summarize texts.

![Image](https://github.com/user-attachments/assets/5e4e53de-0cf1-4896-8070-228c6a42cc54)

## How LLMs Work:

•⚙️ They use transformer architectures to process text and learn context-aware patterns.

•🧠 By identifying patterns in data, they create coherent and relevant responses.

## Benefits of LLMs:

• ⏱️ Automates repetitive tasks like chatbots and drafting emails.

• 💡 Boosts productivity in content creation and research.

• 🤝 Improves human-computer interaction with intelligent, conversational interfaces.


# Explanation of the Code: ♣

Here’s a breakdown of what your code does:

1.Environment Setup:

Loads environment variables securely using dotenv to fetch the API key.

2.Model Initialization:

Connects to the Google Gemini Pro LLM.

Starts a chat session for dynamic and interactive conversations.

3.Streamlit App Initialization:

Creates a Streamlit app with a user-friendly text input field.

Uses session state to preserve chat history during interactions.

4.Real-Time Responses:

Sends user queries to the Gemini LLM.

Receives streamed responses in real-time, chunk by chunk, for faster feedback.

5.Chat History:

Logs the conversation (both user inputs and AI responses) for a full history view.

Allows users to revisit the complete interaction.


## Demo 📽

Below is a demonstration of how the application works:

![Demo of the Application](https://github.com/Abdelrahman-Amen/Q_A_Chatbot_using_LLM/blob/main/Q%26A%20Chatbot%20Demo.gif)
