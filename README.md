# Wake Mate – Keep Your System Awake Effortlessly
# Description:
Wake Mate is a lightweight desktop utility designed to prevent your computer from going to sleep or activating the screensaver. It works by periodically simulating subtle mouse movements, tricking your system into thinking it's active—even when you're not interacting with it directly.
This tool is especially useful during long meetings, online classes, remote sessions, or continuous data processing tasks, where your system must remain awake and responsive without manual input. It features a simple graphical interface with Play, Pause, and Stop buttons for intuitive control.

# Key Features:
- Keeps your system awake by moving the mouse at regular intervals.
- Simple GUI with play/pause/stop controls.
- Clean, distraction-free design.
- Lightweight and runs silently in the background.
- Prevents screen lock, screen dimming, and system sleep.

# Use Case Example:
You're attending a virtual conference that lasts several hours, with long stretches of listening and minimal interaction. Normally, your system would go idle and sleep or lock the screen—interrupting your connection or making it seem like you're inactive. Wake Mate keeps your system engaged, ensuring uninterrupted presence and productivity.

# Required Python Packages:
To run Wake Mate, the following Python packages are required:

```pyautogui``` – to simulate mouse movement.

```pillow``` – to handle image files for GUI icons.

```tkinter``` – for the graphical user interface (standard with most Python installations).

# How to run
- Download all the files under src folder.
- Open your terminal and run the following command - ```python wake_mate.py```
- For windows: You can alternatively download the zip folder and extract it. Then run the win_mate.exe under dist folder
- If you are on mac: You can run the following command to create an exe of the project and run the exe
  ```pyinstaller --onefile --windowed --add-data "icons:icons" --icon=app.ico wake_mate.py```
