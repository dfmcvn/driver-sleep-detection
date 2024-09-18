# Driver Sleepy Detection

**Driver Sleepy Detection** is a Python-based project aimed at detecting drowsiness in drivers through facial recognition techniques and eye behavior analysis. This project is created **for educational and learning purposes only and is not intended for production or commercial use**.

## Project Overview

The main objective of this project is to demonstrate how to use image processing and machine learning techniques to detect when a driver is becoming drowsy. The system can be integrated with a camera that continuously monitors the driver's eyes and alerts the driver if signs of sleepy/drowsy are detected.

### Key Features:
- Detects drowsiness based on eye closure.
- Uses image processing and computer vision techniques such as OpenCV and dlib.
- Alerts the driver when drowsiness is detected (sound notification).

---

## Installation and Setup

To run this project, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/dfmcvn/driver-sleepy-detection.git
    cd driver-sleepy-detection
    ```

2. **Set up a virtual environment (optional but recommended)**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate   # On Windows: .venv\Scripts\activate
    ```

3. **Install required dependencies**:
    The project uses Python and some key libraries such as OpenCV and dlib. Install all dependencies with:
   ```bash
   pip install -r requirements.txt
   ```
    or
   ```bash
   pip install opencv-python dlib pygame tk pyinstaller Pillow
   ```

5. **Run the main script**:
    Once dependencies are installed, you can run the project using the following command:
    ```bash
    python main.py
    ```

---

## Requirements

- Python 3.12
- opencv-python
- dlib
- pygame
- tk
- Pillow

Install all dependencies using the `requirements.txt` file provided.

---

## Usage

This project is designed to be used in a simulated environment. Upon running, the system accesses a webcam (or video feed) to monitor the driver's face. The program will alert the driver if the system detects drowsiness.

Example command:
```bash
python main.py
```

## Limitations

- **Accuracy**: The drowsiness detection system's accuracy may be impacted by various factors, such as lighting conditions, camera quality, or facial obstructions (e.g., glasses or shadows).
- **False Positives/Negatives**: The system may incorrectly detect drowsiness (false positives) or fail to detect it when present (false negatives), making it unsuitable for real-world safety-critical applications.
- **Educational Use Only**: This project is designed purely for **educational and learning purposes**. It is not intended for use in actual driving scenarios or as a substitute for any real-time driver monitoring systems.

---

## Contributing

Contributions, suggestions, and improvements are welcome! Please open a pull request or submit an issue if you'd like to enhance the system, add new features, or fix any bugs.

---

## License

This project is licensed under the MIT License.

---

## Disclaimer

This project is **strictly for educational purposes**. It is not intended for commercial use or deployment in safety-critical environments, such as real-time driver monitoring systems. The system's performance is not guaranteed, and it should not be relied upon for ensuring driver safety.

---

## Acknowledgements

This project was made possible by several open-source libraries. Special thanks to the following communities for their contributions:

- **OpenCV-Python** (https://opencv.org) - For providing powerful tools for real-time image and video processing.
- **dlib** (http://dlib.net) - For facial landmark detection and machine learning algorithms.
- **Pygame** (https://www.pygame.org) - For creating the framework used to handle multimedia and game development, enabling the alert system.
- **Tkinter (tk)** - For providing the user interface framework used to create the application’s graphical interface.
- **Pillow** (https://python-pillow.org) - For image processing capabilities, including image manipulation and file format support.

We greatly appreciate the open-source community's efforts in making these tools freely available.
