import cv2
import dlib
import numpy as np
import sys  # Import sys module


class FaceDetector:
    def __init__(self):
        # Khởi tạo bộ phát hiện khuôn mặt từ dlib
        self.detector = dlib.get_frontal_face_detector()
        try:
            # Sử dụng sys._MEIPASS để lấy đường dẫn đúng đến tệp mô hình khi sử dụng PyInstaller
            model_path = "assets/shape_predictor_68_face_landmarks.dat"
            if hasattr(sys, "_MEIPASS"):
                model_path = f"{sys._MEIPASS}/{model_path}"
            # Tải bộ dự đoán điểm đặc trưng trên khuôn mặt
            self.predictor = dlib.shape_predictor(model_path)
        except RuntimeError:
            print(
                "Lỗi: Không tìm thấy 'shape_predictor_68_face_landmarks.dat'. Vui lòng đảm bảo tệp mô hình tồn tại."
            )
            self.predictor = None

    def detect_faces(self, frame):
        # Đảm bảo khung hình ở định dạng đúng
        if frame is None or frame.size == 0:
            print("Lỗi: Nhận được khung hình trống.")
            return []

        # Chuyển đổi khung hình sang thang độ xám để phát hiện khuôn mặt
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Phát hiện khuôn mặt trong khung hình thang độ xám
        faces = self.detector(gray)
        return list(faces)  # Chuyển đổi dlib.rectangles thành danh sách

    def get_landmarks(self, frame, face):
        # Chuyển đổi khung hình sang thang độ xám để phát hiện điểm đặc trưng
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Phát hiện điểm đặc trưng trên khuôn mặt
        landmarks = self.predictor(gray, face)
        # Chuyển đổi điểm đặc trưng thành mảng numpy của các tọa độ (x, y)
        return np.array([[p.x, p.y] for p in landmarks.parts()])

    def detect_sleep(self, landmarks):
        def eye_aspect_ratio(eye):
            # Kiểm tra xem có đủ điểm để tính toán EAR không
            if len(eye) < 6:
                return 0  # hoặc một giá trị mặc định khác

            # Tính toán khoảng cách cặp giữa các điểm đặc trưng của mắt
            A = np.linalg.norm(eye[1] - eye[5])
            B = np.linalg.norm(eye[2] - eye[4])
            C = np.linalg.norm(eye[0] - eye[3])

            # Tính toán tỷ lệ khía cạnh của mắt
            ear = (A + B) / (2.0 * C)
            return ear

        # Trích xuất điểm đặc trưng cho mắt trái và mắt phải
        left_eye = landmarks[42:48]
        right_eye = landmarks[36:42]
        # Tính toán EAR cho cả hai mắt
        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)
        # Tính toán EAR trung bình
        avg_ear = (left_ear + right_ear) / 2.0

        # Định nghĩa ngưỡng để xác định xem mắt có đóng hay không
        EAR_THRESHOLD = 0.25
        # Trả về True nếu mắt có khả năng đóng, False nếu không
        return avg_ear < EAR_THRESHOLD


# Thêm dòng này vào cuối tệp để chỉ định những gì nên được nhập khi sử dụng "from module import *"
__all__ = ["FaceDetector"]
