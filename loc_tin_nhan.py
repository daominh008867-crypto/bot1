TARGET_GROUP_ID = -1001312892484

def loc_tin_nhan(event):
    """
    Lọc tin nhắn theo Group ID.
    Trả về True nếu đúng nhóm, False nếu không.
    """

    if event.chat_id != TARGET_GROUP_ID:
        return False

    print("=" * 60)
    print("Có tín hiệu mới")
    print(event.raw_text)

    return True