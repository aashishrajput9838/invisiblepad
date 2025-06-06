# Transparent Notepad
python transparent_notepad.py

pyinstaller transparent_notepad.spec

A simple, elegant transparent notepad application that allows you to take notes with a semi-transparent window.

## Features

- Semi-transparent window (90% opacity)
- Draggable window (click and drag the title bar)
- Auto-saves content every 30 seconds
- Persistent storage (content is saved between sessions)
- Clean, minimal interface

## Requirements

- Python 3.x
- tkinter (usually comes with Python installation)

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

- Click and drag the title bar to move the window
- Click the × button in the top-right corner to close the application
- Your notes are automatically saved every 30 seconds
- Content is preserved between sessions

## Notes

- The window is semi-transparent (90% opacity) to allow you to see content behind it
- The window has no standard window decorations for a cleaner look
- All content is saved in a file named `notepad_content.txt` in the same directory as the application 