from luu_cai_dat import (
    tai_toan_bo_cai_dat,
    luu_toan_bo_cai_dat
)

from playsound import playsound
import os


# ==========================
# Đổi nhạc chuông tín hiệu
# ==========================

def doi_nhac_chuong_tin_hieu(file_mp3):
    data = tai_toan_bo_cai_dat()
    data["nhac_chuong"] = file_mp3
    luu_toan_bo_cai_dat(data)


# ==========================
# Đổi nhạc chuông lỗi
# ==========================

def doi_nhac_chuong_loi(file_mp3):
    data = tai_toan_bo_cai_dat()
    data["nhac_chuong_loi"] = file_mp3
    luu_toan_bo_cai_dat(data)


# ==========================
# Nghe thử chuông tín hiệu
# ==========================

def nghe_thu_tin_hieu():
    data = tai_toan_bo_cai_dat()

    file_mp3 = data.get("nhac_chuong", "")

    if os.path.exists(file_mp3):
        playsound(file_mp3)
    else:
        print("Không tìm thấy file nhạc.")


# ==========================
# Nghe thử chuông lỗi
# ==========================

def nghe_thu_loi():
    data = tai_toan_bo_cai_dat()

    file_mp3 = data.get("nhac_chuong_loi", "")

    if os.path.exists(file_mp3):
        playsound(file_mp3)
    else:
        print("Không tìm thấy file nhạc.")