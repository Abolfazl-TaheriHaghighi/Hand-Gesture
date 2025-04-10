# 🎚️ Hand Gesture Volume Control
Control your system volume using your fingers!  
Built with ❤️ using **Python, OpenCV, MediaPipe & Pycaw**

---

## 🖥️ Overview
This project lets you **control your Windows system volume** using just your hand gestures, specifically by measuring the distance between your **thumb and index finger** in real-time via webcam.

---

## 🎯 Features
- 🖐️ Real-time hand tracking with MediaPipe  
- 📊 Dynamic volume bar and percentage display  
- 🔄 Live mirrored camera feed (natural hand movement)  
- 🎚️ System volume control using Pycaw  
- ⌨️ Exit program with `q` key  

---

## 📦 Requirements
Install all dependencies via pip:
```bash
pip install opencv-python mediapipe pycaw comtypes numpy
```

---

## ▶️ How to Run

```bash
python hand_volume_control.py
```

---

## 🎮 Controls

| Gesture               | Action           |
|-----------------------|------------------|
| 🤏 Pinch (close fingers) | Decrease Volume  |
| ✌️ Spread (open fingers) | Increase Volume  |
| 🔴 Press `q`             | Exit Program     |

---

## 📁 Project Files

| File                  | Description           |
|-----------------------|------------------------|
| hand_volume_control.py | Main Python file       |
| README.md              | Project instructions   |

---

## 🧠 Technologies Used
- [x] Python 3.8+
- [x] OpenCV
- [x] MediaPipe (Google)
- [x] Pycaw (Windows Audio API)
- [x] NumPy

---

## 👨‍💻 Author
**Abolfazl Taheri Haghighi**  
📚 Bachelor's student of Statistics, Fasa University  
📍 Iran --> Shiraz
📧 [atahry6@gmail.com]

---

## 📝 License
Free to use for educational & personal purposes.  
For commercial use, please contact the author.

---

## 🔖 Version
**v1.1.0**
