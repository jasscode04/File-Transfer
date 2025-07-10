from tkinter import *
from tkinter import messagebox, filedialog
import socket
import os
import threading

root = Tk()
root.title("Share it")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False, False)

# ================= SEND WINDOW ==================
def Send():
    window = Toplevel(root)
    window.title('Send')
    window.geometry("450x560+500+200")
    window.configure(bg="#f4fdfe")
    window.resizable(False, False)

    def select_file():
        global filename
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File',
                                              filetypes=(('All Files', '*.*'),))

    def sender():
        def send_file():
            try:
                s = socket.socket()
                host = socket.gethostname()
                port = 8080
                s.bind((host, port))
                s.listen(1)
                print("Your ID (Receiver should enter this):", socket.gethostbyname(host))
                print("Waiting for connection...")

                conn, addr = s.accept()
                file = open(filename, 'rb')
                data = file.read(1024)

                while data:
                    conn.send(data)
                    data = file.read(1024)

                file.close()
                conn.close()
                s.close()
                messagebox.showinfo("Success", "File sent successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Send failed:\n{e}")

        threading.Thread(target=send_file).start()  # Run socket code in background

    # Images
    image_icon1 = PhotoImage(file='send.png')
    window.iconphoto(False, image_icon1)
    Sbackground = PhotoImage(file='sender.png')
    Label(window, image=Sbackground).place(x=-2, y=0)
    Mbackground = PhotoImage(file='id.png')
    Label(window, image=Mbackground, bg="#f4fdfe").place(x=100, y=260)

    ip = socket.gethostbyname(socket.gethostname())
    Label(window, text=f'Your ID: {ip}', bg='white', fg='black').place(x=140, y=290)

    Button(window, text='+ Select File', width=15, font='arial 13 bold', bg="#fff", fg="#000",
           command=select_file).place(x=140, y=150)
    Button(window, text='SEND', width=10, font='arial 13 bold', bg='#fff', fg='#000',
           command=sender).place(x=310, y=150)

    # Prevent garbage collection
    window.Sbackground = Sbackground
    window.Mbackground = Mbackground
    window.image_icon1 = image_icon1


# ================= RECEIVE WINDOW ==================
def Receive():
    main = Toplevel(root)
    main.title('Receive')
    main.geometry("450x560+500+200")
    main.configure(bg="#f4fdfe")
    main.resizable(False, False)

    def receiver():
        def receive_file():
            ID = SenderID.get()
            filename1 = incoming_file.get()

            try:
                s = socket.socket()
                port = 8080
                s.connect((ID, port))
                file = open(filename1, 'wb')

                while True:
                    data = s.recv(1024)
                    if not data:
                        break
                    file.write(data)

                file.close()
                s.close()
                messagebox.showinfo("Success", "File received and saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Receive failed:\n{e}")

        threading.Thread(target=receive_file).start()

    image_icon2 = PhotoImage(file='receive.png')
    main.iconphoto(False, image_icon2)
    Hbackground = PhotoImage(file='receiver.png')
    Label(main, image=Hbackground).place(x=-2, y=0)
    logo = PhotoImage(file='profile.png')
    Label(main, image=logo, bg="#f4fdfe").place(x=170, y=200)
    Label(main, text='Receive', font=('arial', 20, 'bold'), bg='#f4fdfe').place(x=170, y=280)

    Label(main, text='Input Sender ID:', font=('arial', 10, 'bold'), bg='#f4fdfe').place(x=20, y=330)
    SenderID = Entry(main, width=25, fg='black', border=2, bg='white', font=('arial', 12))
    SenderID.place(x=20, y=360)
    SenderID.focus()

    Label(main, text='Filename for incoming file:', font=('arial', 10, 'bold'), bg='#f4fdfe').place(x=20, y=410)
    incoming_file = Entry(main, width=25, fg='black', border=2, bg='white', font=('arial', 12))
    incoming_file.place(x=20, y=440)

    imageicon = PhotoImage(file='arrow.png')
    Button(main, image=imageicon, bg="#f4fdfe", bd=0).place(x=370, y=440)

    rr = Button(main, text='Receive', compound=LEFT, image=imageicon, width=130, bg='#39c790',
                font='arial 14 bold', command=receiver)
    rr.place(x=20, y=500)

    # Prevent garbage collection
    main.image_icon2 = image_icon2
    main.Hbackground = Hbackground
    main.logo = logo
    main.imageicon = imageicon


# ========== MAIN WINDOW ==========
icon = PhotoImage(file="icon.png")
root.iconphoto(False, icon)

Label(root, text="File Transfer", font=('Acumin Variable Concept', 20, 'bold'), bg="#f4fdfe").place(x=20, y=30)
Frame(root, width=400, height=2, bg="#f3f5f6").place(x=25, y=80)

send_img = PhotoImage(file="send.png")
send_button = Button(root, image=send_img, bg="#f4fdfe", bd=0, command=Send)
send_button.place(x=50, y=100)

receive_img = PhotoImage(file="receive.png")
receive_button = Button(root, image=receive_img, bg="#f4fdfe", bd=0, command=Receive)
receive_button.place(x=300, y=100)

Label(root, text="Send", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x=65, y=200)
Label(root, text="Receive", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x=300, y=200)

background = PhotoImage(file="background.png")
Label(root, image=background).place(x=-2, y=323)

# Prevent garbage collection
root.send_img = send_img
root.receive_img = receive_img
root.background = background

root.mainloop()
