from telethon import TelegramClient

api_id = 35063634
api_hash = "2459859aaca75bb5541327212e745867"

client = TelegramClient("my_session", api_id, api_hash)


async def kiem_tra_dang_nhap():
    if await client.is_user_authorized():
        me = await client.get_me()
        print(f"Đã ghi nhớ đăng nhập: {me.first_name}")
        return True
    else:
        print("Chưa đăng nhập.")
        return False


async def main():
    if await kiem_tra_dang_nhap():
        return

    # Nếu chưa đăng nhập thì Telethon sẽ yêu cầu đăng nhập
    await client.start()

    me = await client.get_me()
    print(f"Đăng nhập thành công: {me.first_name}")


with client:
    client.loop.run_until_complete(main())