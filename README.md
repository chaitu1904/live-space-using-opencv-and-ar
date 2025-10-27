# 🛰️ Live Space AI: Real-Time AR for Space Optimization

## 📖 Overview
**Live Space AI** is an innovative project that integrates **Computer Vision (OpenCV)** and **Augmented Reality (AR)** to analyze and optimize room space usage in real time.  
By combining **AI-powered object detection** and **AR visualization**, it provides users with intelligent suggestions for efficient room layouts, helping maximize usable space in homes, offices, and studios.

---

## 🎯 Objectives
- Detect and classify real-world objects (like furniture) using AI.  
- Generate real-time AR overlays to suggest optimized object placements.  
- Enhance space utilization dynamically based on object positioning.  
- Provide a foundation for smart, adaptive, IoT-enabled environments.

---

## 🧠 Key Features
✅ Real-time **object detection** using TensorFlow/Keras models.  
✅ **OpenCV-based** room boundary and contour detection.  
✅ **Unity AR Foundation** integration for interactive 3D visualization.  
✅ Live spatial feedback to optimize furniture arrangement.  
✅ Extendable for **IoT** and **robotic space mapping** use cases.  

---

## 🧩 System Architecture
Below is a simplified block flow of the system’s operation:

      ┌────────────────────┐
      │  Camera Input (Live)│
      └──────────┬─────────┘
                 │
                 ▼
       ┌────────────────────┐
       │  Object Detection  │
       │ (OpenCV + TensorFlow) │
       └──────────┬─────────┘
                 │
                 ▼
       ┌────────────────────┐
       │  Space Analysis    │
       │ (Contour Mapping)  │
       └──────────┬─────────┘
                 │
                 ▼
       ┌────────────────────┐
       │ AR Visualization   │
       │ (Unity AR Overlay) │
       └──────────┬─────────┘
                 │
                 ▼
       ┌────────────────────┐
       │ Optimized Layout   │
       │  Suggestions       │
       └────────────────────┘

---

## 🛠️ Tech Stack
| Component | Technology Used |
|------------|----------------|
| Programming Language | Python |
| Computer Vision | OpenCV |
| Deep Learning | TensorFlow / Keras |
| AR Platform | Unity with AR Foundation |
| IDEs | Visual Studio Code, Unity Hub |
| Hardware (Optional) | ESP32 for IoT extensions |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/live-space-ai.git
cd live-space-ai

4️⃣ Unity AR Setup (Optional)

Open the Unity project folder in Unity Hub.

Install AR Foundation and ARCore XR Plugin (via Package Manager).

Connect your mobile device and build the app for Android/iOS.

📜 License

This project is licensed under the MIT License — feel free to use, modify, and distribute it with proper attribution.
