import tkinter as tk
import random

def ask_question():
    """Handles the question asking and response."""
    responses = [
        "It is certain.", "Without a doubt.", "You may rely on it.", "Yes definitely.",
        "It is decidedly so.", "As I see it, yes.", "Most likely.", "Outlook good.",
        "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.",
        "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
        "Don't count on it.", "Outlook not so good.", "My sources say no.",
        "Very doubtful.", "It is decidedly so."
    ]
    question = question_entry.get()
    if question:
        response = random.choice(responses)
        response_label.config(text=response)
    else:
        response_label.config(text="Please enter a question.")

# Main window
root = tk.Tk()
root.title("Magic 8 Ball")

# Question entry
question_label = tk.Label(root, text="Ask the Magic 8 Ball a question:")
question_label.pack(pady=10)

question_entry = tk.Entry(root, width=50)
question_entry.pack(pady=5)

# Ask button
ask_button = tk.Button(root, text="Ask", command=ask_question)
ask_button.pack(pady=10)

# Response label
response_label = tk.Label(root, text="", wraplength=400)
response_label.pack(pady=20)

root.mainloop()
