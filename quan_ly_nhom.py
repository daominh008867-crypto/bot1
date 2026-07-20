from luu_cai_dat import (
    tai_toan_bo_cai_dat,
    luu_toan_bo_cai_dat
)


def tai_danh_sach_nhom():
    cai_dat = tai_toan_bo_cai_dat()
    return cai_dat.get("nhom", [])


def luu_danh_sach_nhom(ds):
    cai_dat = tai_toan_bo_cai_dat()
    cai_dat["nhom"] = ds
    luu_toan_bo_cai_dat(cai_dat)


def them_nhom(ten, group_id):

    ds = tai_danh_sach_nhom()

    ds.append({
        "ten": ten,
        "group_id": group_id,
        "bat": True
    })

    luu_danh_sach_nhom(ds)


def sua_nhom(group_id, ten_moi):

    ds = tai_danh_sach_nhom()

    for nhom in ds:
        if nhom["group_id"] == group_id:
            nhom["ten"] = ten_moi

    luu_danh_sach_nhom(ds)


def xoa_nhom(group_id):

    ds = tai_danh_sach_nhom()

    ds = [n for n in ds if n["group_id"] != group_id]

    luu_danh_sach_nhom(ds)


def bat_tat_nhom(group_id):

    ds = tai_danh_sach_nhom()

    for nhom in ds:
        if nhom["group_id"] == group_id:
            nhom["bat"] = not nhom["bat"]

    luu_danh_sach_nhom(ds)


def hien_thi():

    ds = tai_danh_sach_nhom()

    print("=" * 50)

    for i, nhom in enumerate(ds, start=1):

        trang_thai = "ON" if nhom["bat"] else "OFF"

        print(f"{i}. {nhom['ten']}")
        print(f"ID: {nhom['group_id']}")
        print(f"Trạng thái: {trang_thai}")
        print()