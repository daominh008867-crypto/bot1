
def dem_dieu_kien(text, danh_sach_dieu_kien):
    """
    Đếm số điều kiện xuất hiện trong tin nhắn.

    text : Nội dung Telegram.
    danh_sach_dieu_kien : Danh sách từ khóa cần kiểm tra.
    """

    text = text.upper()

    so_khop = 0
    da_khop = []

    for dk in danh_sach_dieu_kien:

        dk = dk.upper()

        if dk in text:
            so_khop += 1
            da_khop.append(dk)

    return so_khop, da_khop