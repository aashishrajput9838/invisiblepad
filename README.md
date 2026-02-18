# Transparent Notepad

![InvisiblePad Logo](assets/logo/invisiblepad%20logo.png)

A simple, elegant transparent notepad application that allows you to take notes with a semi-transparent window. The application appears in the Windows taskbar while maintaining a clean, minimal interface.

## Quick Start

Run the application:
```bash
python transparent_notepad.py
```

Build executable:
```bash
pyinstaller transparent_notepad.spec
```

## Features

- **Semi-transparent window** - 95% opacity by default, adjustable via controls
- **Taskbar presence** - Appears in Windows taskbar with custom icon
- **Draggable window** - Click and drag the title bar to move the window
- **Auto-save** - Content automatically saved every 30 seconds
- **Persistent storage** - Content preserved between sessions
- **Adjustable opacity** - Increase or decrease transparency using +/- buttons
- **Always-on-top** - Pin the window to stay above other applications
- **Window sizing** - Multiple preset sizes and manual adjustment options
- **Text zoom** - Zoom text in/out with keyboard shortcuts or mouse wheel
- **Full text editing** - Supports all standard text editing operations
- **Scrollable content** - Horizontal and vertical scrollbars for large documents
- **Keyboard shortcuts** - Various shortcuts for enhanced productivity
- **Clean, minimal interface** - Custom title bar with intuitive controls

## Requirements

- Python 3.x
- tkinter (usually comes with Python installation)
- pywin32 (for Windows-specific functionality)
- Pillow (for icon conversion)

## How to Run

1. Make sure you have Python installed on your system
2. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python transparent_notepad.py
   ```

## Usage

- **Moving the window**: Click and drag the title bar to move the window
- **Closing the application**: Click the × button in the top-right corner
- **Adjusting opacity**: Use the +/- buttons in the title bar or Ctrl+Up/Down keys
- **Toggling always-on-top**: Click the "Pin" button to keep the window above others
- **Changing window size**: Click the "Size" button to cycle through preset sizes
- **Zooming text**: Use Ctrl+Plus/Minus or Ctrl+MouseWheel to zoom in/out
- **Resetting zoom**: Press Ctrl+0 to return to default text size
- **Saving content**: Notes are automatically saved every 30 seconds
- **Persistent storage**: All content is saved in `notepad_content.txt`

### Keyboard Shortcuts

- **Alt+T** - Toggle window visibility (completely transparent/opaque)
- **Ctrl+Up/Down** - Increase/decrease window opacity
- **Ctrl+Plus/Minus** - Zoom text in/out
- **Ctrl+MouseWheel** - Zoom text (trackpad)
- **Ctrl+0** - Reset zoom to default
- **Ctrl+Right/Left** - Increase/decrease window width
- **Ctrl+Shift+Up/Down** - Increase/decrease window height
- **Ctrl+A** - Select all text
- **Ctrl+C/V/X** - Copy/Paste/Cut text
- **Ctrl+Z/Y** - Undo/Redo actions

## Notes

- The window is semi-transparent (95% opacity) by default to allow you to see content behind it
- The application appears in the Windows taskbar with a custom icon
- All content is saved in a file named `notepad_content.txt` in the same directory
- The application maintains its position and transparency settings between sessions
- Window decorations are customized for a cleaner, more professional look

## Customizing the Executable Icon

To use a custom icon for the executable (e.g., `invisiblepad logo.png`):

1. Ensure you have Pillow installed: `pip install Pillow`
2. Convert your PNG logo to an ICO format. A script `convert_logo.py` is available for this purpose. Run it using:
   ```
   python convert_logo.py
   ```
   This will generate `invisiblepad_logo.ico`.
3. Update the `transparent_notepad.spec` file to reference `invisiblepad_logo.ico` in the `icon=` parameter of the `EXE` section.
4. Rebuild the executable using PyInstaller:
   ```
   pyinstaller transparent_notepad.spec
   ```
   The executable with the new icon will be in the `dist` directory.

## Download Pre-built Executable

You can download the pre-built executable from the [Releases](https://github.com/aashishrajput9838/invisiblepad/releases) page.

## Building the Executable

To create a standalone executable from source:

1. Install PyInstaller: `pip install pyinstaller`
2. Run the build command:
   ```
   pyinstaller TransparentNotepad.spec
   ```
3. Find the executable in the `dist` folder

## License

© 2025 Aspirinexar. All rights reserved.

This software is developed and maintained by **Aspirinexar**.  
Unauthorized copying, distribution, or modification of this software is strictly prohibited.

![Aspirinexar Logo](assets/logo/aspirinexar%20logo.jpg)

