# import json
# import os

# TEN_FILE = "settings.json"


# def luu_toan_bo_cai_dat(cai_dat):
#     """Lưu toàn bộ cài đặt"""
#     with open(TEN_FILE, "w", encoding="utf-8") as f:
#         json.dump(cai_dat, f, ensure_ascii=False, indent=4)


# def tai_toan_bo_cai_dat():
#     """Đọc toàn bộ cài đặt"""

#     if not os.path.exists(TEN_FILE):
#         return {}

#     with open(TEN_FILE, "r", encoding="utf-8") as f:
#         return json.load(f)
import json
import os

TEN_FILE = "settings.json"

MAC_DINH = {
    "nhom": [],
    "dieu_kien": [],
    "nhac_chuong": "",
    "nhac_chuong_loi": "",
    "popup": True,
    "rung": True,
    "am_luong": 100
}


def luu_toan_bo_cai_dat(cai_dat):
    """Lưu toàn bộ cài đặt"""
    with open(TEN_FILE, "w", encoding="utf-8") as f:
        json.dump(cai_dat, f, ensure_ascii=False, indent=4)


def tai_toan_bo_cai_dat():
    """Đọc toàn bộ cài đặt"""

    if not os.path.exists(TEN_FILE):
        return MAC_DINH.copy()

    with open(TEN_FILE, "r", encoding="utf-8") as f:
        return json.load(f)