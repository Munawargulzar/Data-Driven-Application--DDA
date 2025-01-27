import requests
import tkinter as tk
from PIL import Image, ImageTk


def switch_frame(frame):
    """Switch to a specific frame."""
    for f in frames.values():
        f.pack_forget()
    frame.pack(fill="both", expand=True)


def get_data():
    country_name = entry_box.get().strip()
    if country_name:
        url = f"https://restcountries.com/v3.1/name/{country_name}"
        response = requests.get(url)
        if response.status_code == 200:
            country_data = response.json()[0]
            update_result_frame(country_data)
            switch_frame(result_frame)
        else:
            update_error_frame(f"Error: {response.status_code}")
            switch_frame(error_frame)
    else:
        update_error_frame("Enter a country name!")
        switch_frame(error_frame)


def update_result_frame(country_data):
    """Update the result frame with country data."""
    info = (
        f"Name: {country_data['name']['common']}\n"
        f"Capital: {country_data.get('capital', ['N/A'])[0]}\n"
        f"Continent: {country_data.get('continents', ['N/A'])[0]}\n"
        f"Area: {country_data['area']} sq. km\n"
        f"Population: {country_data['population']}"
    )
    result_label.config(text=info)


def update_error_frame(error_message):
    """Update the error frame with an error message."""
    error_label.config(text=error_message)


def set_background_image(frame, image_path):
    """Set a background image for a frame."""
    image = Image.open(image_path)
    image = image.resize((700, 500), Image.Resampling.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)

    bg_label = tk.Label(frame, image=bg_image)
    bg_label.image = bg_image  # Keep a reference to avoid garbage collection
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Ensure it stays in the background


def add_hover_effect(button, hover_bg, normal_bg):
    """Add hover effect to a button."""
    button.bind("<Enter>", lambda e: button.config(bg=hover_bg))
    button.bind("<Leave>", lambda e: button.config(bg=normal_bg))


# Main Window
window = tk.Tk()
window.geometry("700x600")
window.title("Global Explorer")
window.resizable(0, 0)

# Frame Dictionary
frames = {}

# Start Frame
start_frame = tk.Frame(window)
frames["start"] = start_frame

set_background_image(start_frame, "currency.jpg")  # Set background image for the start frame

title_label = tk.Label(
    start_frame,
    text="Welcome to Global Explorer",
    bg="#FF6F61",  # Coral color
    fg="white",
    font=("Comic Sans MS", 26, "bold"),
    pady=20,
)
title_label.pack(pady=100)

start_button = tk.Button(
    start_frame,
    text="Explore",
    bg="#FF6F61",  # Coral color
    fg="white",
    font=("Comic Sans MS", 16, "bold"),
    command=lambda: switch_frame(main_frame),
)
add_hover_effect(start_button, hover_bg="#FF3B2A", normal_bg="#FF6F61")
start_button.pack(pady=20)

# Main Frame
main_frame = tk.Frame(window)
frames["main"] = main_frame

set_background_image(main_frame, "bgcountry.jpeg")  # Set background image for the main frame

header_label = tk.Label(
    main_frame,
    text="Global Explorer",
    bg="#FF6F61",  # Coral color
    fg="white",
    font=("Comic Sans MS", 26, "bold"),
    pady=15,
)
header_label.pack(fill="x")

entry_label = tk.Label(
    main_frame,
    text="Country Name:",
    bg="#FF6F61",  # Coral color
    fg="white",
    font=("Comic Sans MS", 16, "bold"),
)
entry_label.pack(pady=10)

entry_box = tk.Entry(main_frame, width=25, font=("Comic Sans MS", 16))
entry_box.pack(pady=10)

search_button = tk.Button(
    main_frame,
    text="Get Country Info",
    bg="#FF6F61",  # Coral color
    fg="white",
    font=("Comic Sans MS", 16, "bold"),
    command=get_data,
)
add_hover_effect(search_button, hover_bg="#FF3B2A", normal_bg="#FF6F61")
search_button.pack(pady=20)

footer_label = tk.Label(
    main_frame,
    text="Countries API",
    bg="#FF6F61",  # Coral color
    fg="white",
    font=("Comic Sans MS", 12),
    pady=5,
)
footer_label.pack(side="bottom", fill="x")

# Result Frame
result_frame = tk.Frame(window)
frames["result"] = result_frame

set_background_image(result_frame, "bgcountry.jpeg")  # Set background image

result_header = tk.Label(
    result_frame,
    text="Nation Profile",
    bg="#FF6F61",  # Coral color
    fg="white",
    font=("Comic Sans MS", 26, "bold"),
    pady=15,
)
result_header.pack(fill="x")

result_label = tk.Label(
    result_frame,
    text="",
    bg="white",
    fg="black",
    font=("Comic Sans MS", 16),
    padx=20,
    pady=20,
    relief="groove",
    borderwidth=2,
)
result_label.pack(pady=20)

back_button = tk.Button(
    result_frame,
    text="Back",
    bg="#FF6F61",  # Coral color
    fg="white",
    font=("Comic Sans MS", 16, "bold"),
    command=lambda: switch_frame(main_frame),
)
add_hover_effect(back_button, hover_bg="#FF3B2A", normal_bg="#FF6F61")
back_button.pack(pady=10)

# Error Frame
error_frame = tk.Frame(window)
frames["error"] = error_frame

set_background_image(error_frame, "bgcountry.jpeg")  # Set background image

error_header = tk.Label(
    error_frame,
    text="Error",
    bg="#B22222",  # Dark Red color for error
    fg="white",
    font=("Comic Sans MS", 26, "bold"),
    pady=15,
)
error_header.pack(fill="x")

error_label = tk.Label(
    error_frame,
    text="",
    bg="#FFD2D2",  # Light Red for the error message
    fg="black",
    font=("Comic Sans MS", 16),
    padx=20,
    pady=20,
)
error_label.pack(pady=20)

error_back_button = tk.Button(
    error_frame,
    text="Back",
    bg="#B22222",  # Dark Red color for error
    fg="white",
    font=("Comic Sans MS", 16, "bold"),
    command=lambda: switch_frame(main_frame),
)
add_hover_effect(error_back_button, hover_bg="#FF6347", normal_bg="#B22222")
error_back_button.pack(pady=10)

# Start with Start Frame
switch_frame(start_frame)

window.mainloop()