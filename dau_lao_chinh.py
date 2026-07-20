from luu_cai_dat import (
    tai_toan_bo_cai_dat,
    luu_toan_bo_cai_dat
)

from bat_tat import TelegramAlarm
from phat_chuong import phat_chuong


# ======================================
# Khởi động ứng dụng
# ======================================

def khoi_dong():

    cai_dat = tai_toan_bo_cai_dat()

    # Nếu chưa có cài đặt thì tạo mặc định
    if not cai_dat:

        cai_dat = {
            "nhom": [],
            "dieu_kien": [],
            "nhac_chuong": "",
            "nhac_chuong_loi": "",
            "popup": True,
            "rung": True,
            "am_luong": 100,
            "ung_dung_bat": False
        }

        luu_toan_bo_cai_dat(cai_dat)

    print("Đã đọc toàn bộ cài đặt.")

    return cai_dat


# ======================================
# Chạy ứng dụng
# ======================================

if __name__ == "__main__":

    cai_dat = khoi_dong()

    app = TelegramAlarm()

    try:
        app.run()

    finally:
        # Lưu lại trước khi thoát
        luu_toan_bo_cai_dat(cai_dat)
        print("Đã lưu toàn bộ cài đặt.")