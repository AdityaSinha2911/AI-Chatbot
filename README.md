# AI GUI Chatbot (Desktop Application)

A desktop-based AI chatbot built using Python and Tkinter.  
The application connects to an AI API to generate real-time responses within a graphical interface.

## Features

- Graphical chat interface using Tkinter  
- Real-time AI responses via API  
- Enter key and button support  
- Scrollable chat window  
- Configurable system prompt for personalization  

## Tech Stack

- Python  
- Tkinter  
- Requests (HTTP communication)  
- OpenRouter / OpenAI-compatible API  

## Installation

1. Clone the repository:

   git clone https://github.com/your-username/your-repo-name.git  
   cd your-repo-name  

2. Install dependencies:

   pip install requests  

3. Add your API key inside `chatbot.py`:

   API_KEY = "YOUR_API_KEY_HERE"

4. Run the application:

   python chatbot.py  

## Configuration

You can modify the system prompt in the code to control the chatbot’s personality:

   SYSTEM_PROMPT = "You are a helpful AI assistant."

## Overview

The application sends user input to an AI model using a REST API and displays the generated response inside a desktop chat window. It demonstrates GUI development, event-driven programming, and API integration in Python.
