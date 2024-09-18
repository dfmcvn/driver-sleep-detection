import pygame


class AudioManager:
    def __init__(self):
        # Khởi tạo pygame mixer để phát âm thanh
        pygame.mixer.init()
        try:
            # Cố gắng tải tệp âm thanh báo động
            self.alarm_sound = pygame.mixer.Sound("assets/alarm.wav")
        except pygame.error:
            # Nếu không tìm thấy tệp, in thông báo lỗi và đặt alarm_sound thành None
            print("Lỗi: Không tìm thấy 'alarm.wav'. Vui lòng đảm bảo tệp âm thanh tồn tại.")
            self.alarm_sound = None

    def play_alarm(self):
        # Phát âm thanh báo động nếu nó đã được tải thành công
        if self.alarm_sound:
            self.alarm_sound.play()

    def stop_alarm(self):
        # Dừng âm thanh báo động nếu nó đã được tải thành công và đang phát
        if self.alarm_sound:
            self.alarm_sound.stop()
