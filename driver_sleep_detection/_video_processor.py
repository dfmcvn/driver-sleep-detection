
import cv2

class VideoProcessor:
    def __init__(self, face_detector, gui, audio_manager):
        # Initialize the VideoProcessor with necessary components
        self.face_detector = face_detector
        self.gui = gui
        self.audio_manager = audio_manager
        
        # Initialize counters for sleep detection
        self.sleep_frames = 0
        self.awake_frames = 0
        # Define thresholds for sleep and awake states
        self.SLEEP_THRESHOLD = 15
        self.AWAKE_THRESHOLD = 5

    def process_frame(self, frame):
        # Resize the frame to match the GUI video frame dimensions
        frame = cv2.resize(frame, (self.gui.video_frame.winfo_width(), self.gui.video_frame.winfo_height()))
        # Detect faces in the frame
        faces = self.face_detector.detect_faces(frame)

        is_sleeping = False

        for face in faces:
            # Get facial landmarks for each detected face
            landmarks = self.face_detector.get_landmarks(frame, face)
            # Determine if the face is showing signs of sleep
            face_sleeping = self.face_detector.detect_sleep(landmarks)

            if face_sleeping:
                # Increment sleep frame counter and reset awake frame counter
                self.sleep_frames += 1
                self.awake_frames = 0
            else:
                # Increment awake frame counter
                self.awake_frames += 1
                # If awake for long enough, reset sleep frame counter
                if self.awake_frames >= self.AWAKE_THRESHOLD:
                    self.sleep_frames = 0

            # Determine if the person is considered sleeping based on the threshold
            is_sleeping = self.sleep_frames >= self.SLEEP_THRESHOLD

            # Set rectangle color based on sleep state (green for awake, red for sleeping)
            color = (0, 255, 0) if not is_sleeping else (0, 0, 255)
            # Draw rectangle around the detected face
            cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), color, 2)

        # Update the GUI with the processed frame
        self.gui.update_video(frame)

        # Play or stop the alarm based on the sleep state
        if is_sleeping:
            self.audio_manager.play_alarm()
        else:
            self.audio_manager.stop_alarm()

        # Return the current sleep state
        return is_sleeping