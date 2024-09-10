import tkinter as tk
from function import word_conversion
import pyttsx3
import time
from collections import defaultdict
import threading


def display_text(event=None):
    user_input = search_bar.get().lower().split()  # Split into individual keywords
    keywords_matched = defaultdict(int)  # Use defaultdict for flexibility

    # Check for individual keywords and update counts
    for keyword in user_input:
        for full_phrase, response in word_conversion.items():
            if keyword in full_phrase.lower().split():
                keywords_matched[full_phrase] += 1

    # Identify the most matched phrase for response
    max_matches = max(keywords_matched.values(), default=0)
    best_response = None
    for phrase, count in keywords_matched.items():
        if count == max_matches:
            best_response = phrase
            break  # Exit early if multiple phrases have the same max count

    # Display response or default message if no match
    if best_response:
        output_label.config(text=word_conversion[best_response])
    else:
        output_label.config(text="Sorry, I couldn't understand your request.")

    search_bar.delete(0, tk.END)

    # Create a thread to speak the response asynchronously
    thread = threading.Thread(target=speak_response, args=(output_label.cget("text"),))
    thread.start()

def speak_response(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# def display_text(event=None):
#     user_input = search_bar.get().lower().split()  # Split into individual keywords
#     keywords_matched = defaultdict(int)  # Use defaultdict for flexibility

#     # Check for individual keywords and update counts
#     for keyword in user_input:
#         for full_phrase, response in word_conversion.items():
#             if keyword in full_phrase.lower().split():
#                 keywords_matched[full_phrase] += 1

#     # Identify the most matched phrase for response
#     max_matches = max(keywords_matched.values(), default=0)
#     best_response = None
#     for phrase, count in keywords_matched.items():
#         if count == max_matches:
#             best_response = phrase
#             break  # Exit early if multiple phrases have the same max count

#     # Display response or default message if no match
#     if best_response:
#         output_label.config(text=word_conversion[best_response])
#     else:
#         output_label.config(text="Sorry, I couldn't understand your request.")
#     search_bar.delete(0, tk.END)

#     time.sleep(10) 
#     engine = pyttsx3.init()
#     engine.say(output_label.cget("text"))
#     engine.runAndWait()
    

# Create the main window
root = tk.Tk()
root.title("NodeMCU project")
root.state('zoomed')
root.geometry("1920x1080")  # Set the initial window size
root.configure(bg="black")  # Set the background color to black
# Create a label to display the text in the middle
screen_width = root.winfo_screenwidth()
wraplength = int(0.6 * screen_width)  # Adjust the factor (0.6) as desired
output_label = tk.Label(root, text="", font=("Arial", 24), fg="white", bg="black" , width = wraplength , wraplength=wraplength)  # Set a fixed width
output_label.place(relx=0.5, rely=0.4, anchor="center")

# Create a canvas to draw the custom rounded search bar
canvas = tk.Canvas(root, bg="white", highlightthickness=0)
canvas.place(relx=0.1, rely=0.9, relwidth=0.8, relheight=0.08)  # Position and size the canvas

# Variables for the design
search_bar_radius = 10  # Adjust the radius for the curved corners

# Draw the rounded rectangle for the search bar background
canvas.create_arc((0, 0, 2 * search_bar_radius, 2 * search_bar_radius), start=90, extent=90, fill="white", outline="white")  # Top-left corner
canvas.create_arc((canvas.winfo_width() - 2 * search_bar_radius, 0, canvas.winfo_width(), 2 * search_bar_radius), start=0, extent=90, fill="white", outline="white")  # Top-right corner
canvas.create_arc((0, canvas.winfo_height() - 2 * search_bar_radius, 2 * search_bar_radius, canvas.winfo_height()), start=180, extent=90, fill="white", outline="white")  # Bottom-left corner
canvas.create_arc((canvas.winfo_width() - 2 * search_bar_radius, canvas.winfo_height() - 2 * search_bar_radius, canvas.winfo_width(), canvas.winfo_height()), start=270, extent=90, fill="white", outline="white")  # Bottom-right corner
canvas.create_rectangle((search_bar_radius, 0, canvas.winfo_width() - search_bar_radius, canvas.winfo_height()), fill="white", outline="white")  # Middle rectangle

# Create an Entry widget (search bar) on top of the rounded rectangle
search_bar = tk.Entry(root, font=("Arial", 14), bd=0, highlightthickness=0, relief="flat")
search_bar.configure(justify='center')  # Center the text inside the search bar
search_bar.place(relx=0.1, rely=0.9, relwidth=0.8, relheight=0.08)  # Position and size the search bar

# Bind the Enter key to the display_text function
search_bar.bind("<Return>", display_text)

# Create a square button (blue) on the right side of the search bar
button = tk.Button(root, text="", command=display_text, font=("Arial", 14), bg="blue", fg="white")
button.place(relx=0.85, rely=0.9, relwidth=0.1, relheight=0.08)  # Position and size the button
# Run the application
root.mainloop()
