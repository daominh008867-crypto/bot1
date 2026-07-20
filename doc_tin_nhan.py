from telethon import TelegramClient, events

api_id = 35063634
api_hash = "API_HASH_CỦA_BẠN"

client = TelegramClient("my_session", api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    print("==========")
    print("Nhóm:", event.chat.title if event.chat else "Private")
    print("Người gửi:", event.sender_id)
    print("Tin nhắn:")
    print(event.raw_text)

print("Đang lắng nghe tin nhắn...")

client.start()
client.run_until_disconnected()