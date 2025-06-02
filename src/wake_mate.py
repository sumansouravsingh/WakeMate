import threading
import time
import tkinter as tk
import sys
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
import pyautogui
import logging
from pathlib import Path

# -------------------- Configuration --------------------

ICON_DIR = Path("icons")
MOVE_INTERVAL = 60  # seconds between actions
MOVE_DURATION = 1  # duration of mouse movement in seconds
POS_X, POS_Y = 5, 5
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class WakeMateApp:
    """Class """
    def __init__(self, root):
        """Initialize the WakeMateApp.
            Args:
                root (tk.Tk): The root window instance from tkinter.
        """
        self.root = root
        self.root.title("Wake Mate")
        self.root.geometry("236x60")
        self.screen_width, self.screen_height = pyautogui.size()
        self.current_x, self.current_y = POS_X, POS_Y
        self.is_running = False
        self.worker_thread = None
        self._load_icons()
        self._build_gui()

    def get_resource_path(self, relative_path):
        """Get absolute path to resource, works for dev and for PyInstaller"""
        try:
            base_path = Path(sys._MEIPASS)
        except AttributeError:
            base_path = Path(__file__).parent
        return base_path / relative_path

    def _load_icons(self):
        """Loads the play, pause, and stop icons from the icons directory.
            Raises an error dialog and exits the app if loading fails.
        """
        try:
            self.play_img = ImageTk.PhotoImage(Image.open(self.get_resource_path("icons/play.png")).resize((32, 32)))
            self.pause_img = ImageTk.PhotoImage(Image.open(self.get_resource_path("icons/pause.png")).resize((32, 32)))
            self.stop_img = ImageTk.PhotoImage(Image.open(self.get_resource_path("icons/stop.png")).resize((32, 32)))
            logging.info(self.play_img)
        except Exception as e:
            logging.error("Failed to load icons: %s", e)
            messagebox.showerror("Error", "Could not load icons.")
            self.root.destroy()

    def _build_gui(self):
        """Builds the graphical user interface and places the control buttons (play, pause, stop)"""
        play_button = tk.Button(self.root, image=self.play_img, command=self.start)
        pause_button = tk.Button(self.root, image=self.pause_img, command=self.pause)
        stop_button = tk.Button(self.root, image=self.stop_img, command=self.stop)

        play_button.grid(row=0, column=0, padx=20, pady=10)
        pause_button.grid(row=0, column=1, padx=20, pady=10)
        stop_button.grid(row=0, column=2, padx=20, pady=10)

    def _worker(self):
        """
            Background thread function that moves the mouse and types periodically.
            Continues until the `self.is_running` flag is set to False.
        """
        try:
            while self.is_running:
                self.current_x = self.current_x + 1 if self.current_x + 1 < self.screen_width else POS_X
                self.current_y = self.current_y + 1 if self.current_y + 1 < self.screen_height else POS_Y
                pyautogui.moveTo(self.current_x, self.current_y, duration=MOVE_DURATION)
                logging.info("Mouse moved and text typed.")
                time.sleep(MOVE_INTERVAL)
        except Exception as e:
            logging.exception("Error in worker thread: %s", e)

    def start(self):
        """Starts the background automation by launching the worker thread."""
        if not self.is_running:
            self.is_running = True
            self.worker_thread = threading.Thread(target=self._worker, daemon=True)
            self.worker_thread.start()
            messagebox.showinfo("Action", "Started")
            logging.info("Automation started.")

    def pause(self):
        """Pauses the automation by setting the running flag to False"""
        if self.is_running:
            self.is_running = False
            messagebox.showinfo("Action", "Paused")
            logging.info("Automation paused.")

    def stop(self):
        """Stops the automation and resets the cursor position"""
        if self.is_running:
            self.is_running = False
            logging.info("Automation stopped.")
        self.current_x, self.current_y = POS_X, POS_Y
        messagebox.showinfo("Action", "Stopped and Reset")
        logging.info("Position reset.")

# -------------------- Main --------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = WakeMateApp(root)
    root.mainloop()

