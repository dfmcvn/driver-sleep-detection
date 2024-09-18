import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2

class GUI:
    def __init__(self, window):
        # Initialize the main window
        self.window = window
        self.window.title("Driver Sleep Detection")

        # Calculate window size based on screen dimensions
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)
        self.window.geometry(f"{window_width}x{window_height}")

        # Create and set up GUI widgets
        self.create_widgets()

    def create_widgets(self):
        # Create a frame to hold the video display
        self.video_frame = ttk.Frame(self.window)
        self.video_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Create a label to display the video feed
        self.video_label = ttk.Label(self.video_frame)
        self.video_label.pack(expand=True, fill=tk.BOTH)

    def update_video(self, frame):
        # Convert the frame from BGR to RGB color space
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Create a PIL Image object from the numpy array
        image = Image.fromarray(frame_rgb)
        # Convert PIL Image to PhotoImage for Tkinter
        photo = ImageTk.PhotoImage(image)
        # Update the video label with the new image
        self.video_label.config(image=photo)
        # Keep a reference to prevent garbage collection
        self.video_label.image = photo