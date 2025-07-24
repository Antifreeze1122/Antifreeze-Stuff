import time
import tkinter as tk
from PIL import Image, ImageTk
import sys
import os

def add_to_startup():


    startup_folder = os.path.join(os.environ['APPDATA'], r'Microsoft\Windows\Start Menu\Programs\Startup')
    shortcut_path = os.path.join(startup_folder, "CheeseReminder.lnk")

    if os.path.exists(shortcut_path):
        # Shortcut already exists
        return

    if getattr(sys, 'frozen', False):
        target = sys.executable
    else:
        target = os.path.abspath(sys.argv[0])

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = os.path.dirname(target)
    shortcut.IconLocation = target
    shortcut.save()
    print(f"Created startup shortcut at {shortcut_path}")

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

img_path = os.path.join(base_path, "cheese.png")

def show_popup():
    root = tk.Tk()
    root.title("Cheese")
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.lift()

    original = Image.open(img_path)
    resized = original.copy()
    resized.thumbnail((300, 300))
    img = ImageTk.PhotoImage(resized)

    img_label = tk.Label(root, image=img)
    img_label.image = img
    img_label.pack(padx=20, pady=10)

    label = tk.Label(root, text="Cheese", font=("Arial", 14))
    label.pack(pady=(0, 10))

    root.update_idletasks()
    w = root.winfo_width()
    h = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (w // 2)
    y = (root.winfo_screenheight() // 2) - (h // 2)
    root.geometry(f"{w}x{h}+{x}+{y}")

    root.after(2000, root.destroy)
    root.mainloop()

if __name__ == "__main__":
    add_to_startup()
    try:
        while True:
            show_popup()
            time.sleep(7 * 60 * 60)  # 7 hours
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)
