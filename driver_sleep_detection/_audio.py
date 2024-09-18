import pygame

class AudioManager:
    def __init__(self):
        # Initialize the pygame mixer for audio playback
        pygame.mixer.init()
        try:
            # Attempt to load the alarm sound file
            self.alarm_sound = pygame.mixer.Sound("assets/alarm.wav")
        except pygame.error:
            # If the file is not found, print an error message and set alarm_sound to None
            print("Error: 'alarm.wav' not found. Please ensure the audio file exists.")
            self.alarm_sound = None

    def play_alarm(self):
        # Play the alarm sound if it has been successfully loaded
        if self.alarm_sound:
            self.alarm_sound.play()

    def stop_alarm(self):
        # Stop the alarm sound if it has been successfully loaded and is currently playing
        if self.alarm_sound:
            self.alarm_sound.stop()