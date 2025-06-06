import win32gui
import win32con # Added win32con as it's used with GCL_STYLE

try:
    if hasattr(win32gui, 'SetClassLongPtr'):
        print("win32gui.SetClassLongPtr is available.")
    else:
        print("win32gui does not have the attribute SetClassLongPtr.")
except AttributeError as e:
    print(f"Caught AttributeError: {e}")
except Exception as e:
    print(f"Caught unexpected exception: {e}")