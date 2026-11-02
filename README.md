# 🐶 Emotion-Based Dog Filter

An interactive AI-powered computer vision project that detects human facial expressions and transforms them into fun animal filters in real time.

## ✨ About the Project

The Emotion-Based Dog Filter combines facial detection, emotion recognition, and image processing to create an interactive webcam experience.

Using a webcam, the application detects a person's face, analyses their facial expression, and applies an animal mask corresponding to the detected emotion.

### 🎭 Emotion-Based Filters

| Detected Emotion | Applied Filter |
|---|---|
| Happy 😊 | Dog 🐶 |
| Sad 😢 | Dalmatian 🐾 |
| Surprised 😮 | Cat 🐱 |

## 🚀 Features

- Real-time face detection using OpenCV.
- Facial emotion recognition using a pretrained PyTorch model.
- Automatic animal filter selection based on detected emotions.
- Live webcam integration.
- Multiple animal masks.
- Image processing and facial landmark-related utilities.

## 🛠️ Technologies Used

- Python
- OpenCV
- PyTorch
- NumPy
- Computer Vision
- Convolutional Neural Networks (CNN)

## 📁 Project Structure

```text
emotion-based-dog-filter/
│
├── src/
│   ├── assets/
│   ├── data/
│   ├── outputs/
│   ├── step_2_face_detect.py
│   ├── step_3_camera_test.py
│   ├── step_7_fer.py
│   └── step_8_dog_emotion_mask.py
│
├── requirements.txt
├── setup_windows.bat
├── run_filter.bat
├── test_webcam.bat
├── README.md
└── LICENSE
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.12 (64-bit)
- VS Code
- A working webcam
- Windows operating system

### 1. Clone the Repository

```bash
git clone https://github.com/kritikaaa2020-lang/emotion-based-dog-filter.git
```

### 2. Navigate to the Project

```bash
cd emotion-based-dog-filter
```

### 3. Set Up the Environment

Run the Windows setup script:

```powershell
.\setup_windows.bat
```

This creates a virtual environment and installs the required dependencies.

### 4. Launch the Application

```powershell
.\run_filter.bat
```

Allow webcam access if prompted.

Press **Q** to close the application.

## 🧠 How It Works

1. **Face Detection:** OpenCV identifies faces in the webcam feed.
2. **Emotion Recognition:** A pretrained PyTorch model analyses facial expressions.
3. **Emotion Classification:** The application identifies the predicted emotion.
4. **Filter Selection:** An animal mask is selected according to the detected emotion.
5. **Real-Time Processing:** The mask is applied to the webcam feed.

## 🎯 Project Objectives

- Explore practical applications of artificial intelligence.
- Understand facial expression recognition.
- Implement real-time computer vision.
- Combine deep learning with image processing.
- Develop an interactive AI-based application.

## 🔮 Future Improvements

- Improve facial detection and mask alignment.
- Add more emotions and animal filters.
- Develop a browser-based version.
- Improve real-time processing performance.
- Create a more interactive user interface.

## 👩‍💻 Author

**Kritika**

GitHub: [@kritikaaa2020-lang](https://github.com/kritikaaa2020-lang)

---

*An exploration of artificial intelligence, computer vision, and creative image processing.*

*Original project inspiration: Alvin Wan's 2017 emotion-based dog filter tutorial. This repository contains a modified project setup and performance improvements.*
