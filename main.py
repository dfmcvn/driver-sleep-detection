# Import necessary libraries
import cv2  # OpenCV for image processing
import tkinter as tk  # GUI library

# Import custom modules for driver sleep detection
from driver_sleep_detection._face_detection import FaceDetector
from driver_sleep_detection._gui import GUI
from driver_sleep_detection._audio import AudioManager
from driver_sleep_detection._video_processor import VideoProcessor

# Installation instructions for dependencies
# Install dependencies: `pip install opencv-python dlib pygame tk pyinstaller Pillow`
# or `pip install -U -r requirements.txt`
# Also install tkinter on MacOS: `brew install python-tk@3.12`

class DriverSleepDetectionApp:
    def __init__(self, window):
        # Initialize the main application window
        self.window = window
        # Create GUI instance
        self.gui = GUI(window)
        # Initialize face detector
        self.face_detector = FaceDetector()
        # Initialize audio manager for alerts
        self.audio_manager = AudioManager()
        # Initialize video processor with necessary components
        self.video_processor = VideoProcessor(
            self.face_detector, self.gui, self.audio_manager
        )

        # Open the default camera (index 0)
        self.cap = cv2.VideoCapture(0)
        # Check if the camera is accessible
        if not self.cap.isOpened():
            print("Error: Unable to access the camera/webcam.")
            self.window.quit()
            return
        # Bind 'q' key to quit the application
        self.window.bind("<q>", self.quit_app)

        # Start processing video frames
        self.process_video()

    def process_video(self):
        # Read a frame from the camera
        ret, frame = self.cap.read()
        if ret:
            # Process the frame if successfully captured
            self.video_processor.process_frame(frame)

        # Schedule the next frame processing after 10 milliseconds
        self.window.after(10, self.process_video)

    def quit_app(self, event=None):
        # Release the camera
        self.cap.release()
        # Close the tkinter window
        self.window.quit()
        self.window.destroy()


if __name__ == "__main__":
    # Create the main tkinter window
    root = tk.Tk()
    # Initialize the DriverSleepDetectionApp
    app = DriverSleepDetectionApp(root)
    # Start the tkinter event loop
    root.mainloop()
