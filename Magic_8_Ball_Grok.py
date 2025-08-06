import tkinter as tk
from tkinter import messagebox
import random

def ask_question():
    """Handles the question asking and response."""
    responses = [
        "It is certain.", "Without a doubt.", "You may rely on it.", "Yes definitely.",
        "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
        "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
        "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.",
        "Outlook not so good.", "My sources say no.", "Very doubtful."
    ]
    question = question_entry.get().strip()  # Remove whitespace
    if question:
        response = random.choice(responses)
        response_label.config(text=response)
        # Optionally clear the entry field after asking
        question_entry.delete(0, tk.END)
    else:
        response_label.config(text="Please enter a valid question.")

def clear_input():
    """Clears the input field and response label."""
    question_entry.delete(0, tk.END)
    response_label.config(text="")

def on_closing():
    """Handles window closing with confirmation."""
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

try:
    # Main window
    root = tk.Tk()
    root.title("Magic 8 Ball")
    root.geometry("500x300")  # Set window size
    root.resizable(True, True)  # Allow resizing
    root.minsize(400, 200)  # Minimum window size

    # Question entry
    question_label = tk.Label(root, text="Ask the Magic 8 Ball a question:")
    question_label.pack(pady=10)

    question_entry = tk.Entry(root, width=50)
    question_entry.pack(pady=5)
    question_entry.focus_set()  # Set focus on entry field
    question_entry.bind("<Return>", lambda event: ask_question())  # Bind Enter key

    # Button frame for Ask and Clear buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    # Ask button
    ask_button = tk.Button(button_frame, text="Ask", command=ask_question)
    ask_button.pack(side=tk.LEFT, padx=5)

    # Clear button
    clear_button = tk.Button(button_frame, text="Clear", command=clear_input)
    clear_button.pack(side=tk.LEFT, padx=5)

    # Response label
    response_label = tk.Label(root, text="", wraplength=450)
    response_label.pack(pady=20)

    # Handle window close
    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

except Exception as e:
    print(f"Error initializing Tkinter: {e}")
