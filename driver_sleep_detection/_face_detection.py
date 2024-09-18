import cv2
import dlib
import numpy as np

class FaceDetector:
    def __init__(self):
        # Initialize the face detector from dlib
        self.detector = dlib.get_frontal_face_detector()
        try:
            # Load the facial landmark predictor
            self.predictor = dlib.shape_predictor("assets/shape_predictor_68_face_landmarks.dat")
        except RuntimeError:
            print("Error: 'shape_predictor_68_face_landmarks.dat' not found. Please ensure the model file exists.")
            self.predictor = None

    def detect_faces(self, frame):
        # Ensure the frame is in the correct format
        if frame is None or frame.size == 0:
            print("Error: Empty frame received.")
            return []

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detect faces in the grayscale frame
        faces = self.detector(gray)
        return list(faces)  # Convert dlib.rectangles to a list

    def get_landmarks(self, frame, face):
        # Convert the frame to grayscale for landmark detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detect facial landmarks
        landmarks = self.predictor(gray, face)
        # Convert landmarks to a numpy array of (x, y) coordinates
        return np.array([[p.x, p.y] for p in landmarks.parts()])

    def detect_sleep(self, landmarks):
        def eye_aspect_ratio(eye):
            # Check if we have enough points to calculate EAR
            if len(eye) < 6:
                return 0  # or some other default value

            # Calculate pairwise distances between eye landmarks
            A = np.linalg.norm(eye[1] - eye[5])
            B = np.linalg.norm(eye[2] - eye[4])
            C = np.linalg.norm(eye[0] - eye[3])
            
            # Calculate the eye aspect ratio
            ear = (A + B) / (2.0 * C)
            return ear

        # Extract landmarks for left and right eyes
        left_eye = landmarks[42:48]
        right_eye = landmarks[36:42]
        # Calculate EAR for both eyes
        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)
        # Calculate the average EAR
        avg_ear = (left_ear + right_ear) / 2.0

        # Define the threshold for determining if eyes are closed
        EAR_THRESHOLD = 0.25
        # Return True if eyes are likely closed, False otherwise
        return avg_ear < EAR_THRESHOLD

# Add this line at the end of the file to specify what should be imported when using "from module import *"
__all__ = ['FaceDetector']
