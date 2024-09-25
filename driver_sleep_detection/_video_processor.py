import cv2


class VideoProcessor:
    def __init__(self, face_detector, gui, audio_manager):
        # Khởi tạo VideoProcessor với các thành phần cần thiết
        self.face_detector = face_detector
        self.gui = gui
        self.audio_manager = audio_manager

        # Khởi tạo bộ đếm cho việc phát hiện ngủ gật
        self.sleep_frames = 0
        self.awake_frames = 0
        # Định nghĩa ngưỡng cho trạng thái ngủ và tỉnh táo
        self.SLEEP_THRESHOLD = 15
        self.AWAKE_THRESHOLD = 5

    def process_frame(self, frame):
        # Check if the GUI is paused
        if self.gui.is_paused:
            return False

        # Đảm bảo khung hình ở định dạng đúng
        if frame is None or frame.size == 0:
            print("Lỗi: Nhận được khung hình trống.")
            return False

        # Thay đổi kích thước khung hình để khớp với kích thước khung video của GUI
        frame = cv2.resize(
            frame,
            (self.gui.video_frame.winfo_width(), self.gui.video_frame.winfo_height()),
        )
        # Phát hiện khuôn mặt trong khung hình
        faces = self.face_detector.detect_faces(frame)

        is_sleeping = False

        for face in faces:
            # Lấy các điểm đặc trưng trên khuôn mặt cho mỗi khuôn mặt được phát hiện
            landmarks = self.face_detector.get_landmarks(frame, face)
            # Xác định xem khuôn mặt có dấu hiệu ngủ gật hay không
            face_sleeping = self.face_detector.detect_sleep(landmarks)

            if face_sleeping:
                # Tăng bộ đếm khung hình ngủ và đặt lại bộ đếm khung hình tỉnh táo
                self.sleep_frames += 1
                self.awake_frames = 0
            else:
                # Tăng bộ đếm khung hình tỉnh táo
                self.awake_frames += 1
                # Nếu tỉnh táo đủ lâu, đặt lại bộ đếm khung hình ngủ
                if self.awake_frames >= self.AWAKE_THRESHOLD:
                    self.sleep_frames = 0

            # Xác định xem người đó có được coi là đang ngủ dựa trên ngưỡng hay không
            is_sleeping = self.sleep_frames >= self.SLEEP_THRESHOLD

            # Đặt màu hình chữ nhật dựa trên trạng thái ngủ (xanh lá cây cho tỉnh táo, đỏ cho ngủ)
            color = (0, 255, 0) if not is_sleeping else (0, 0, 255)
            # Vẽ hình chữ nhật xung quanh khuôn mặt được phát hiện
            cv2.rectangle(
                frame,
                (face.left(), face.top()),
                (face.right(), face.bottom()),
                color,
                2,
            )

        # Cập nhật GUI với khung hình đã xử lý
        self.gui.update_video(frame)

        # Phát hoặc dừng âm báo dựa trên trạng thái ngủ
        if is_sleeping:
            self.audio_manager.play_alarm()
        else:
            self.audio_manager.stop_alarm()

        # Trả về trạng thái ngủ hiện tại
        return is_sleeping
