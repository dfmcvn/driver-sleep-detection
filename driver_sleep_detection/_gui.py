import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import time


class GUI:
    def __init__(self, window):
        # Khởi tạo cửa sổ chính
        self.window = window
        self.window.title("Driver Sleep Detection")

        # Tính toán kích thước cửa sổ dựa trên kích thước màn hình
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)
        self.window.geometry(f"{window_width}x{window_height}")

        # Tạo và thiết lập các widget của GUI
        self.create_widgets()

    def create_widgets(self):
        # Tạo một khung để hiển thị video
        self.video_frame = ttk.Frame(self.window)
        self.video_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Tạo một nhãn để hiển thị luồng video
        self.video_label = ttk.Label(self.video_frame)
        self.video_label.pack(expand=True, fill=tk.BOTH)

        # Add FPS label
        self.fps_label = ttk.Label(
            self.video_frame, text="FPS: 0", background="black", foreground="white"
        )
        self.fps_label.place(x=10, y=10)

        # Initialize FPS calculation variables
        self.frame_count = 0
        self.start_time = time.time()

    def update_video(self, frame):
        # Increment frame count
        self.frame_count += 1

        # Calculate elapsed time
        elapsed_time = time.time() - self.start_time

        # Update FPS every 1 second
        if elapsed_time >= 1:
            fps = self.frame_count / elapsed_time
            self.fps_label.config(text=f"FPS: {fps:.2f}", foreground="red")
            self.frame_count = 0
            self.start_time = time.time()

        # Chuyển đổi khung hình từ không gian màu BGR sang RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Tạo một đối tượng PIL Image từ mảng numpy
        image = Image.fromarray(frame_rgb)
        # Chuyển đổi PIL Image thành PhotoImage cho Tkinter
        photo = ImageTk.PhotoImage(image)
        # Cập nhật nhãn video với hình ảnh mới
        self.video_label.config(image=photo)
        # Giữ một tham chiếu để tránh việc bị xoá bỏ
        self.video_label.image = photo
