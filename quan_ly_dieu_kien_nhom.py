import json
import os

FILE_NAME = "groups.json"


def tai_du_lieu():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)


def luu_du_lieu(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# ==========================
# Thêm điều kiện
# ==========================

def them_dieu_kien(group_id, dieu_kien):

    data = tai_du_lieu()

    for nhom in data:

        if nhom["group_id"] == group_id:

            if dieu_kien not in nhom["dieu_kien"]:
                nhom["dieu_kien"].append(dieu_kien)

    luu_du_lieu(data)


# ==========================
# Xóa điều kiện
# ==========================

def xoa_dieu_kien(group_id, dieu_kien):

    data = tai_du_lieu()

    for nhom in data:

        if nhom["group_id"] == group_id:

            if dieu_kien in nhom["dieu_kien"]:
                nhom["dieu_kien"].remove(dieu_kien)

    luu_du_lieu(data)


# ==========================
# Sửa điều kiện
# ==========================

def sua_dieu_kien(group_id, cu, moi):

    data = tai_du_lieu()

    for nhom in data:

        if nhom["group_id"] == group_id:

            for i in range(len(nhom["dieu_kien"])):

                if nhom["dieu_kien"][i] == cu:
                    nhom["dieu_kien"][i] = moi

    luu_du_lieu(data)


# ==========================
# Đổi số điều kiện cần khớp
# ==========================

def doi_so_dieu_kien(group_id, so):

    data = tai_du_lieu()

    for nhom in data:

        if nhom["group_id"] == group_id:
            nhom["so_dieu_kien"] = so

    luu_du_lieu(data)


# ==========================
# Hiển thị
# ==========================

def hien_thi_dieu_kien(group_id):

    data = tai_du_lieu()

    for nhom in data:

        if nhom["group_id"] == group_id:

            print("=" * 50)
            print("Tên nhóm:", nhom["ten"])
            print()

            print("Điều kiện:")

            for dk in nhom["dieu_kien"]:
                print("-", dk)

            print()
            print("Số điều kiện cần khớp:", nhom["so_dieu_kien"])