import cv2
import tkinter as tk

from driver_sleep_detection._face_detection import FaceDetector
from driver_sleep_detection._gui import GUI
from driver_sleep_detection._audio import AudioManager
from driver_sleep_detection._video_processor import VideoProcessor


class DriverSleepDetectionApp:
    def __init__(self, window):
        # Khởi tạo cửa sổ chính
        self.window = window
        # Khởi tạo GUI
        self.gui = GUI(window)
        # Khởi tạo bộ phát hiện khuôn mặt
        self.face_detector = FaceDetector()
        # Khởi tạo quản lý âm thanh
        self.audio_manager = AudioManager()
        # Khởi tạo bộ xử lý video
        self.video_processor = VideoProcessor(
            self.face_detector, self.gui, self.audio_manager
        )

        # Mở camera/webcam
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            # Nếu không thể truy cập camera/webcam, in thông báo lỗi và thoát ứng dụng
            print("Error: Unable to access the camera/webcam.")
            self.window.quit()
            return
        # Gán phím 'q' để thoát ứng dụng
        self.window.bind("<q>", self.quit_app)

        # Bắt đầu xử lý video
        self.process_video()

    def process_video(self):
        # Đọc khung hình từ camera/webcam
        ret, frame = self.cap.read()
        if ret:
            # Xử lý khung hình
            self.video_processor.process_frame(frame)

        # Gọi lại hàm này sau 10ms
        self.window.after(10, self.process_video)

    def quit_app(self, event=None):
        # Giải phóng camera/webcam và thoát ứng dụng
        self.cap.release()
        self.window.quit()
        self.window.destroy()


if __name__ == "__main__":
    # Tạo cửa sổ Tkinter và chạy ứng dụng
    root = tk.Tk()
    app = DriverSleepDetectionApp(root)
    root.mainloop()
