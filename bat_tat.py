from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.switch import Switch
from kivy.uix.label import Label


class MainScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=20, **kwargs)

        # Tiêu đề
        self.add_widget(Label(
            text="Telegram Alarm",
            font_size=28,
            size_hint=(1, 0.15)
        ))

        # Dòng bật/tắt
        row = BoxLayout(
            orientation="horizontal",
            size_hint=(1, 0.15)
        )

        self.status = Label(
            text="🔴 Ứng dụng: OFF",
            font_size=22
        )

        self.switch = Switch(active=False)
        self.switch.bind(active=self.change_status)

        row.add_widget(self.status)
        row.add_widget(self.switch)

        self.add_widget(row)

        # Trạng thái Telegram
        self.telegram = Label(
            text="Telegram: Chưa chạy",
            font_size=20
        )
        self.add_widget(self.telegram)

        # Trạng thái Internet
        self.internet = Label(
            text="Internet: Chưa kiểm tra",
            font_size=20
        )
        self.add_widget(self.internet)

    def change_status(self, instance, value):

        if value:

            self.status.text = "🟢 Ứng dụng: ON"
            self.telegram.text = "Telegram: Đang theo dõi"
            self.internet.text = "Internet: Đang kiểm tra..."

        else:

            self.status.text = "🔴 Ứng dụng: OFF"
            self.telegram.text = "Telegram: Đã dừng"
            self.internet.text = "Internet: Không theo dõi"


class TelegramAlarm(App):

    def build(self):
        return MainScreen()


TelegramAlarm().run()