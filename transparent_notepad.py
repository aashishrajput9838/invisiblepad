import tkinter as tk
from tkinter import ttk
import json
import os
import win32gui
import win32con
from tkinter import font as tkfont

class TransparentNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Transparent Notepad")
        
        # Initialize always on top state
        self.always_on_top = False
        
        # Make window transparent
        self.transparency = 0.95
        self.root.attributes('-alpha', self.transparency)
        
        # Remove window decorations and do not show in taskbar
        self.root.overrideredirect(True)
        
        # Get the window handle
        self.hwnd = win32gui.GetForegroundWindow()
        
        # Create main frame
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create title bar
        self.title_bar = ttk.Frame(self.main_frame)
        self.title_bar.pack(fill=tk.X)
        
        # Title label with modern font
        title_font = tkfont.Font(family="Segoe UI", size=10)
        self.title_label = ttk.Label(self.title_bar, text="Transparent Notepad", font=title_font)
        self.title_label.pack(side=tk.LEFT, padx=5)
        
        # Transparency controls
        self.transparency_label = ttk.Label(self.title_bar, text="Opacity:", font=title_font)
        self.transparency_label.pack(side=tk.LEFT, padx=(10, 0))
        
        # Add percentage label
        self.percentage_label = ttk.Label(self.title_bar, text="95%", font=title_font)
        self.percentage_label.pack(side=tk.LEFT, padx=(0, 5))
        
        # Minus button
        self.minus_button = tk.Button(
            self.title_bar,
            text="−",
            width=2,
            font=title_font,
            bg="#0078d4",
            fg="white",
            relief="flat",
            command=lambda: self.adjust_transparency(-0.05)
        )
        self.minus_button.pack(side=tk.LEFT, padx=(5, 0))
        
        # Plus button
        self.plus_button = tk.Button(
            self.title_bar,
            text="+",
            width=2,
            font=title_font,
            bg="#0078d4",
            fg="white",
            relief="flat",
            command=lambda: self.adjust_transparency(0.05)
        )
        self.plus_button.pack(side=tk.LEFT, padx=(2, 5))
        
        # Always on top button
        self.always_on_top_button = tk.Button(
            self.title_bar,
            text="Pin",
            width=4,
            font=title_font,
            bg="#0078d4",
            fg="white",
            relief="flat",
            command=self.toggle_always_on_top
        )
        self.always_on_top_button.pack(side=tk.RIGHT, padx=(0, 2))
        
        # Size button
        self.size_button = tk.Button(
            self.title_bar,
            text="Size",
            width=4,
            font=title_font,
            bg="#0078d4",
            fg="white",
            relief="flat",
            command=self.toggle_size
        )
        self.size_button.pack(side=tk.RIGHT, padx=(0, 2))
        
        # Close button
        self.close_button = tk.Button(
            self.title_bar,
            text="×",
            width=3,
            font=title_font,
            bg="#0078d4",
            fg="white",
            relief="flat",
            command=self.root.quit
        )
        self.close_button.pack(side=tk.RIGHT)
        
        # Create text area with modern font
        self.text_area = tk.Text(
            self.main_frame,
            wrap=tk.NONE,  # Disable text wrapping
            font=('Segoe UI', 10),
            relief='flat',
            padx=10,
            pady=10
        )
        
        # Add scrollbars
        self.v_scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.text_area.yview)
        self.h_scrollbar = ttk.Scrollbar(self.main_frame, orient="horizontal", command=self.text_area.xview)
        
        # Configure text area to use scrollbars
        self.text_area.configure(
            yscrollcommand=self.v_scrollbar.set,
            xscrollcommand=self.h_scrollbar.set
        )
        
        # Pack scrollbars and text area
        self.v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Initialize zoom level
        self.zoom_level = 10  # Default font size
        self.min_zoom = 6    # Minimum font size
        self.max_zoom = 24   # Maximum font size
        
        # Bind zoom events
        self.text_area.bind('<Control-MouseWheel>', self.zoom_text)  # For trackpad
        self.text_area.bind('<Control-plus>', lambda e: self.zoom_text(e, 1))  # Ctrl + Plus
        self.text_area.bind('<Control-minus>', lambda e: self.zoom_text(e, -1))  # Ctrl + Minus
        self.text_area.bind('<Control-0>', self.reset_zoom)  # Ctrl + 0 to reset zoom
        
        # Enable drag and drop
        self.text_area.bind('<Button-1>', self.start_drag)
        self.text_area.bind('<B1-Motion>', self.on_drag)
        self.text_area.bind('<ButtonRelease-1>', self.stop_drag)
        self.text_area.bind('<Control-a>', self.select_all)
        
        # Bind mouse events for dragging
        self.title_bar.bind('<Button-1>', self.start_move)
        self.title_bar.bind('<B1-Motion>', self.on_move)
        
        # Bind keyboard shortcut for toggling visibility
        self.root.bind('<Alt-t>', self.toggle_visibility)
        
        # Bind keyboard shortcuts for transparency
        self.root.bind('<Control-Up>', lambda e: self.adjust_transparency(0.05))
        self.root.bind('<Control-Down>', lambda e: self.adjust_transparency(-0.05))
        
        # Bind keyboard shortcuts for window size
        self.root.bind('<Control-Right>', lambda e: self.adjust_width(50))
        self.root.bind('<Control-Left>', lambda e: self.adjust_width(-50))
        self.root.bind('<Control-Shift-Up>', lambda e: self.adjust_height(50))
        self.root.bind('<Control-Shift-Down>', lambda e: self.adjust_height(-50))
        
        # Bind keyboard shortcuts
        self.text_area.bind('<Control-c>', self.copy_text)
        self.text_area.bind('<Control-v>', self.paste_text)
        self.text_area.bind('<Control-x>', self.cut_text)
        self.text_area.bind('<Control-z>', self.undo_text)
        self.text_area.bind('<Control-y>', self.redo_text)
        
        # Load saved content
        self.load_content()
        
        # Auto-save every 30 seconds
        self.root.after(30000, self.auto_save)
        
        # Add hover effects for buttons
        for button in [self.minus_button, self.plus_button, self.always_on_top_button, self.close_button]:
            button.bind('<Enter>', lambda e, b=button: self.on_button_hover(b))
            button.bind('<Leave>', lambda e, b=button: self.on_button_leave(b))
    
    def on_button_hover(self, button):
        button.configure(bg='#106ebe')  # Darker blue on hover
    
    def on_button_leave(self, button):
        button.configure(bg="#0078d4")
    
    def toggle_visibility(self, event=None):
        if self.transparency == 0.0:
            self.transparency = 0.95
        else:
            self.transparency = 0.0
        self.root.attributes('-alpha', self.transparency)
    
    def adjust_transparency(self, delta):
        new_transparency = self.transparency + delta
        # Keep transparency between 0.0 and 1.0
        new_transparency = max(0.0, min(1.0, new_transparency))
        self.transparency = new_transparency
        self.root.attributes('-alpha', self.transparency)
        # Update percentage label
        percentage = int(self.transparency * 100)
        self.percentage_label.config(text=f"{percentage}%")
        
    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def on_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")

    def save_content(self):
        content = self.text_area.get("1.0", tk.END)
        with open("notepad_content.txt", "w", encoding="utf-8") as f:
            f.write(content)

    def load_content(self):
        try:
            with open("notepad_content.txt", "r", encoding="utf-8") as f:
                content = f.read()
                self.text_area.insert("1.0", content)
        except FileNotFoundError:
            pass

    def auto_save(self):
        self.save_content()
        self.root.after(30000, self.auto_save)

    # Method to set window always on top
    def toggle_always_on_top(self):
        try:
            # Get the current window handle
            self.hwnd = win32gui.GetForegroundWindow()
            if self.hwnd:
                win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
                self.always_on_top_button.config(text="Pinned", foreground="red")
                self.always_on_top = True
            else:
                print("Window handle not found.")
        except Exception as e:
            print(f"Error setting always on top: {e}")

    def toggle_size(self):
        # Get current window size
        current_width = self.root.winfo_width()
        current_height = self.root.winfo_height()
        
        # Define size presets
        sizes = [
            (400, 300),  # Default size
            (600, 400),  # Medium size
            (800, 600),  # Large size
            (300, 200)   # Small size
        ]
        
        # Find next size
        current_size = (current_width, current_height)
        try:
            current_index = sizes.index(current_size)
            next_index = (current_index + 1) % len(sizes)
        except ValueError:
            next_index = 0
            
        # Apply new size
        new_width, new_height = sizes[next_index]
        self.root.geometry(f"{new_width}x{new_height}")

    def start_drag(self, event):
        # Store the starting position
        self.drag_start = self.text_area.index(f"@{event.x},{event.y}")
        # Start selection
        self.text_area.tag_remove("sel", "1.0", "end")
        self.text_area.tag_add("sel", self.drag_start)
        # Configure text area for drag and drop
        self.text_area.config(cursor="arrow")
        
    def on_drag(self, event):
        try:
            # Get current position
            current = self.text_area.index(f"@{event.x},{event.y}")
            # Update selection
            self.text_area.tag_remove("sel", "1.0", "end")
            self.text_area.tag_add("sel", self.drag_start, current)
        except tk.TclError:
            pass
            
    def stop_drag(self, event):
        try:
            # Get end position
            end = self.text_area.index(f"@{event.x},{event.y}")
            # Get selected text
            selected_text = self.text_area.get("sel.first", "sel.last")
            # Delete selected text
            self.text_area.delete("sel.first", "sel.last")
            # Insert at new position
            self.text_area.insert(end, selected_text)
            # Reset cursor
            self.text_area.config(cursor="")
        except tk.TclError:
            # Reset cursor if no selection
            self.text_area.config(cursor="")
            
    def select_all(self, event):
        self.text_area.tag_add("sel", "1.0", "end")
        return "break"  # Prevent default behavior

    def copy_text(self, event=None):
        try:
            # Get selected text
            selected_text = self.text_area.get("sel.first", "sel.last")
            # Clear clipboard and set new text
            self.root.clipboard_clear()
            self.root.clipboard_append(selected_text)
        except tk.TclError:
            pass
        return "break"  # Prevent default behavior
        
    def paste_text(self, event=None):
        try:
            # Get clipboard content
            clipboard_text = self.root.clipboard_get()
            # Insert at current position or selection
            try:
                self.text_area.delete("sel.first", "sel.last")
            except tk.TclError:
                pass
            self.text_area.insert("insert", clipboard_text)
        except tk.TclError:
            pass
        return "break"  # Prevent default behavior
        
    def cut_text(self, event=None):
        try:
            # Get selected text
            selected_text = self.text_area.get("sel.first", "sel.last")
            # Clear clipboard and set new text
            self.root.clipboard_clear()
            self.root.clipboard_append(selected_text)
            # Delete selected text
            self.text_area.delete("sel.first", "sel.last")
        except tk.TclError:
            pass
        return "break"  # Prevent default behavior

    def undo_text(self, event=None):
        try:
            self.text_area.edit_undo()
        except tk.TclError:
            pass
        return "break"  # Prevent default behavior
        
    def redo_text(self, event=None):
        try:
            self.text_area.edit_redo()
        except tk.TclError:
            pass
        return "break"  # Prevent default behavior

    def adjust_width(self, delta):
        current_width = self.root.winfo_width()
        new_width = max(300, current_width + delta)  # Minimum width of 300
        self.root.geometry(f"{new_width}x{self.root.winfo_height()}")
        
    def adjust_height(self, delta):
        current_height = self.root.winfo_height()
        new_height = max(200, current_height + delta)  # Minimum height of 200
        self.root.geometry(f"{self.root.winfo_width()}x{new_height}")

    def zoom_text(self, event, delta=None):
        if delta is None:
            # For trackpad scroll
            delta = 1 if event.delta > 0 else -1
            
        # Calculate new zoom level
        new_zoom = self.zoom_level + delta
        
        # Keep zoom within limits
        if self.min_zoom <= new_zoom <= self.max_zoom:
            self.zoom_level = new_zoom
            # Update font size
            self.text_area.configure(font=('Segoe UI', self.zoom_level))
            # Update scrollbars
            self.text_area.see("insert")  # Keep cursor visible
            
        return "break"  # Prevent default behavior
        
    def reset_zoom(self, event=None):
        self.zoom_level = 10  # Reset to default
        self.text_area.configure(font=('Segoe UI', self.zoom_level))
        # Update scrollbars
        self.text_area.see("insert")  # Keep cursor visible
        return "break"  # Prevent default behavior

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")
    app = TransparentNotepad(root)
    root.mainloop() 