import socket
from playsound import playsound


# ==========================
# Kiểm tra Internet
# ==========================

def kiem_tra_internet():

    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True

    except:
        return False


# ==========================
# Báo lỗi Internet
# ==========================

def bao_loi_internet():

    print("=" * 60)
    print("❌ MẤT KẾT NỐI INTERNET")

    playsound("error.mp3")


# ==========================
# Báo lỗi Telegram
# ==========================

def bao_loi_telegram():

    print("=" * 60)
    print("❌ TELEGRAM ĐÃ NGẮT KẾT NỐI")

    playsound("error.mp3")