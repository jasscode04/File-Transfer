
# 📁 Share It — File Transfer App using Python

A GUI-based Python project to **send and receive files** over a local network using **sockets** and **Tkinter**. This app allows two users to connect via IP and transfer any type of file with a user-friendly interface.

---

## 🖼️ App UI

- **Send Window**: Select a file and share your IP address for the receiver to connect.
- **Receive Window**: Enter sender's IP and desired filename to receive and save the file.
- **Custom Icons and Backgrounds** for polished aesthetics.

---

## 🚀 Features

✅ File sending and receiving over local network  
✅ Real-time connection using `socket`  
✅ Multithreaded background transfer  
✅ GUI interface using `Tkinter`  
✅ Pop-up alerts on success or failure  
✅ Stylish images and icons for send/receive windows

---

## 🧑‍💻 Technologies Used

- **Python 3**
- **Tkinter** for GUI
- **Socket** for networking
- **Threading** for non-blocking file transfer
- **OS** and **filedialog** for file selection

---

## 📸 Preview

| Send Window | Receive Window |
|-------------|----------------|
| ![send](send.png) | ![receive](receive.png) |

---

## 📂 Folder Structure

```
project/
│
├── icon.png
├── send.png
├── receive.png
├── sender.png
├── receiver.png
├── arrow.png
├── profile.png
├── background.png
├── share_it.py       ← (main Python file)
└── README.md
```

---

## 💡 How It Works

### 🔵 On Sender Side:
1. Launch the app and click **Send**
2. Select the file you want to share
3. Share your **IP address** (displayed on screen) with the receiver
4. Click **SEND** and wait for connection

### 🟢 On Receiver Side:
1. Launch the app and click **Receive**
2. Enter the **Sender's IP address**
3. Enter the **filename** you want to save the file as
4. Click **Receive** and the file will be downloaded

---

## ⚙️ How to Run

1. Install Python (if not already)
2. Place all `.png` image assets in the same folder as `share_it.py`
3. Run the script:

```bash
python share_it.py
```

4. Make sure **both sender and receiver are on the same network**

---

## 🔐 Security Note

This app is designed for **local network testing only**. For real-world use:
- Add encryption (e.g. `ssl`)
- Add authentication and file validation
- Consider using unique ports or dynamic socket bindings

---

## 📌 Future Improvements

- Drag and drop file selection  
- Real-time progress bar  
- Support for folders/zipped files  
- Dark mode toggle  
- Encrypted transfer over Internet

---

## 🤝 Author

**Jasprit Singh Sanu**  
Python + Django Developer | AI Enthusiast  
[GitHub: jasscode04](https://github.com/jasscode04)
