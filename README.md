# Virtual Mouse Project

## Overview
The Virtual Mouse Project simulates mouse interactions using hand gestures detected through a webcam. It uses computer vision techniques to track hand movements and performs actions such as clicking and double-clicking.

## Features
- Real-time hand tracking using a webcam.
- Gesture-based control for:
  - Left click.
  - Double click.

## Prerequisites
Ensure the following software and libraries are installed on your system:

- **Python 3.7 or later**
- Required Python Libraries:
  ```bash
  pip install opencv-python mediapipe numpy pyautogui
  ```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/rishraks/Virtual_Mouse.git
   cd virtual-mouse
   ```
2. Install dependencies:
   ```bash
   pip install opencv-python mediapipe numpy pyautogui
   ```
3. Run the project:
   ```bash
   python Virtual_Mouse.py
   ```

## Usage
1. Launch the program.
2. Ensure your webcam is enabled and your hand is visible within the frame.
3. Use predefined gestures to control the mouse:
   - **Left Click**: Tap index finger and thumb together once.
   - **Double Click**: Tap index finger and thumb together twice quickly.

## File Structure
```
virtual-mouse/
├── env/                  # Virtual environment for dependencies
├── Virtual_Mouse.py      # Main script for running the project
├── LICENSE               # License for the project
└── README.md             # Project documentation
```

## How It Works
1. **Hand Detection**: The project uses [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html) for real-time hand detection and landmark identification.
2. **Gesture Recognition**: Predefined rules map hand gestures to mouse actions.
3. **Mouse Control**: The [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) library interacts with the system to simulate mouse clicks.

## Customization
- **Modify Gestures**: Update the gesture logic in `Virtual_Mouse.py` to include new gestures or tweak existing ones.
- **Change Sensitivity**: Adjust parameters within the script to control responsiveness.
- **Add Features**: Extend functionality by adding new gestures or integrating additional libraries.

## Limitations
- Performance may vary under poor lighting conditions.
- Accuracy depends on the background and hand visibility.

## Future Improvements
- Add support for right-click and scroll gestures.
- Implement a graphical interface for configuration and usage.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements
- [OpenCV](https://opencv.org/)
- [MediaPipe](https://google.github.io/mediapipe/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)

