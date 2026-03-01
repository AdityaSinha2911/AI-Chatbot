import tkinter as tk
import requests
import json
import threading
from openai import OpenAI



# i have taken open router api key
API_KEY = "your api key"

# OpenRouter API endpoint
API_URL = "https://openrouter.ai/api/v1/chat/completions"

SYSTEM_PROMPT = "You are a helpful and intelligent AI assistant."

# saves conversation for further chats
conversation = [
    {"role": "system", "content": SYSTEM_PROMPT}
]


# AI RESPONSE FUNCTION

def get_ai_response(user_message):

    conversation.append({"role": "user", "content": user_message})

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Tkinter Chatbot"
    }

    data = {
        # model changed, openrouter/auto will choose the free tier model automatically.
        "model": "openrouter/auto",  
        "messages": [
            {"role": "user", "content": user_message}]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=30)

        # error handling part improved.
        if response.status_code != 200:
            return f"API Error {response.status_code}:\n{response.text}"

        result = response.json()

        if "choices" not in result:
            return "Unexpected API response:\n" + str(result)

        message = result["choices"][0]["message"]

        reply = message.get("content")
       

        conversation.append({
            "role": "assistant",
            "content": reply,
        })


        return reply

    except Exception as e:
        return "Error: " + str(e)

# thread function added

def process_message(user_text):

    try:
        reply = get_ai_response(user_text)

        # Update GUI safely using after()
        root.after(0, display_reply, reply)

    except Exception as e:
        root.after(0, display_reply, "Error: " + str(e))


# display function

def display_reply(reply):

    # Remove "Thinking..." line
    chat_area.delete("end-2l", "end-1l")

    chat_area.insert(tk.END, "Bot: " + reply + "\n\n")
    chat_area.see(tk.END)


# SEND MESSAGE FUNCTION

def send_message(event=None):

    user_text = entry_box.get()

    if user_text.strip() == "":
        return

    # Show user message
    chat_area.insert(tk.END, "You: " + user_text + "\n")
    chat_area.see(tk.END)

    entry_box.delete(0, tk.END)

    # Show thinking message
    chat_area.insert(tk.END, "Bot: Thinking...\n")
    chat_area.see(tk.END)
    
    # Start new thread for API call
    #threads are made safer
    thread = threading.Thread(target=process_message, args=(user_text,), daemon=True)
    thread.start()


# CLEAR CHAT FUNCTION
def clear_chat():
    global conversation
    chat_area.delete(1.0, tk.END)

    conversation = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]


# GUI SETUP

root = tk.Tk()
root.title("AI Chatbot")
root.geometry("500x600")
root.resizable(True, True)


# Chat display area
chat_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


# Scrollbar
scrollbar = tk.Scrollbar(chat_area)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_area.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=chat_area.yview)


# Bottom frame
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill=tk.X, padx=10, pady=5)


# Entry box
entry_box = tk.Entry(bottom_frame, font=("Arial", 12))
entry_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

# Send button
send_button = tk.Button(bottom_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT)


# Enter key support
entry_box.bind("<Return>", send_message)


root.mainloop()



