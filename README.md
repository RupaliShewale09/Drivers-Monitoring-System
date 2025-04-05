# Drivers-Monitoring-System  
~ Eye & Mouth Activity Recognition (EAR & MAR)


## 📌 Overview
This project is an **Eye and Mouth Activity Recognition System** that detects **eye closure (EAR) and mouth openness (MAR)** using facial landmark detection. It is useful for applications such as **drowsiness detection, facial expression analysis, and head pose estimation**. 

With the increasing demand for **driver safety, fatigue monitoring, and AI-based human behavior analysis**, this system provides an efficient way to track **eye blinking patterns and yawning frequency** in real time. By integrating **computer vision and AI-driven facial analysis**, this tool enhances user safety and productivity across various domains.

## 🚀 Features
- **Facial Landmark Detection:** Uses `dlib` for detecting facial landmarks.
- **EAR Calculation:** Detects eye closure levels to determine possible drowsiness.
- **MAR Calculation:** Measures mouth openness for detecting yawning or speech.
- **Head Pose Estimation:** Determines head orientation using facial landmarks.
- **Audio Alerts:** Generates warnings using **text-to-speech (TTS)** when drowsiness is detected.
- **Real-time Processing:** Works in real-time using **OpenCV**.
- **Lightweight & Efficient:** Optimized for fast performance on standard hardware.
- **Customizable Thresholds:** Users can adjust EAR and MAR thresholds based on their needs.
- **Daily Database Logging**: Stores real-time logs in SQLite with daily and cumulative tables

## 🛠️ Requirements
Ensure you have the following dependencies installed before running the project:

```plaintext
dlib==19.22.99
imutils==0.5.4
numpy==1.23.5
opencv-python==4.11.0.86
pygame==2.6.1
pyttsx3==2.98
scipy==1.13.1
sqlite3
tk
```

To install all dependencies at once, run:
```bash
pip install -r requirement.txt
```

## 📂 Project Structure
```
├── EAR.py         # Computes Eye Aspect Ratio (EAR) for eye closure detection
├── MAR.py         # Computes Mouth Aspect Ratio (MAR) for yawning detection
├── headpose.py    # Determines head pose using facial landmarks
├── SQL.py             # Database handler for logging drowsiness events in SQLite
├── displayDB.py       # GUI script to display logged drowsiness events by date
├── main.py        # Main script integrating all components
├── requirements.txt  # Required libraries
├── README.md      # Project documentation
```
##📅 Shape Predictor File

This project uses dlib's 68-point facial landmark predictor.

📌 After downloading:                                          
Extract the .bz2 file to get shape_predictor_68_face_landmarks.dat                                    
Place it in the root directory of this project.                                    
This file is essential for facial landmark detection.                                    

## 🖼️ How It Works
- The system detects facial landmarks using **dlib's pre-trained model**.
- It calculates the **Eye Aspect Ratio (EAR)** to determine **eye closure**.
- It calculates the **Mouth Aspect Ratio (MAR)** to detect **mouth openness**.
- If drowsiness is detected (eyes closed or yawning), an **audio alert is triggered**.
- Head pose estimation helps in understanding the **direction of attention**.
- Logs are stored in a SQLite database with timestamp, EAR, MAR, yaw angle, and status.
- Users can open displayDB.py to browse the logs via a GUI.

The project integrates **machine learning, computer vision, and signal processing** techniques to create an intelligent **drowsiness and fatigue monitoring system**. It is an essential tool for applications requiring **non-intrusive human activity recognition**.

## 📌 Applications
✅ **Drowsiness Detection** for drivers and machine operators 🚗                                  
✅ **Fatigue Monitoring** in workplaces 🏢                               
✅ **Facial Expression Analysis** for research and interactive AI 😃                               
✅ **Human-Computer Interaction** in AI-driven applications 💻                               
✅ **Security & Surveillance** for automated monitoring 🎥                               

## 🤝 Contributing
Feel free to fork this repository, submit issues, and make pull requests to improve this project!

---
💡 **Developed with Python & OpenCV for AI-driven facial analysis!**

