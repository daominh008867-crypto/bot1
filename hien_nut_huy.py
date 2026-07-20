import tkinter as tk


def huy_chuong():

    print("Đã tắt chuông")

    cua_so.destroy()


def hien_popup():

    global cua_so

    cua_so = tk.Tk()

    cua_so.title("Thông báo")

    cua_so.geometry("300x150")

    label = tk.Label(
        cua_so,
        text="🔔 Có tín hiệu mới!",
        font=("Arial", 14)
    )

    label.pack(pady=20)

    nut = tk.Button(
        cua_so,
        text="HỦY",
        font=("Arial", 12),
        command=huy_chuong
    )

    nut.pack()

    cua_so.mainloop()