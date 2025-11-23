# 🟢 Invisible Cloak Project (Lime Green Color Cloaking)  
### Developed by: **Mayush Sharma**

This project uses **Computer Vision** (OpenCV + Python) to create an **Invisible Cloak Effect**.  
Whenever the webcam detects **lime green color**, that region becomes **transparent** by replacing it with the captured background.

This project is inspired by the popular "Harry Potter Invisible Cloak" effect — recreated using real-time video processing.

---

## 🚀 Features

- Real-time webcam processing  
- Detects **lime green** objects accurately  
- Removes that color region and shows *only the background*  
- Smooth output with morphological operations  
- Lightweight 50-line implementation  
- Beginner-friendly and easy to customize  

---

## 🧠 How It Works

1. The program first captures a **clean background frame** (without the user).  
2. Every new frame from the webcam is converted to **HSV color space**.  
3. The code detects a specific HSV range for **lime green color**.  
4. The detected lime green region is **masked out**.  
5. That masked region is replaced with the **stored background**,  
   giving the effect that the lime green object is *invisible*.  

---

## 🎯 Lime Green HSV Range Used

```python
lower_lime = np.array([25, 52, 72])
upper_lime = np.array([102, 255, 255])
