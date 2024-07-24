import customtkinter as ctk


# Initialize the app
app = ctk.CTk()
app.title("Social Media Toolkit")
app.geometry("500x500")

# Shared button
from oprations import on_button_click
download_media_button = ctk.CTkButton(app, text="Analyze URL and Download", command=on_button_click, width=300,
                                      height=60, corner_radius=50, fg_color="#1a73e8", hover_color="#1557b2")
# Shared entry
entry = ctk.CTkEntry(app, width=430, placeholder_text="Enter a URL", height=45, corner_radius=30)
entry.pack(pady=65)
