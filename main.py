import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from PIL import Image, ImageDraw, ImageTk
import math


class ModernDrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Drawing App")
        self.root.geometry("1000x650")
        self.root.config(bg="#333333")

        # Customizable Brush
        self.drawing = False
        self.last_x, self.last_y = None, None
        self.brush_color = "#000000"
        self.brush_size = 5
        self.brush_opacity = 255
        self.history = []
        self.redo_history = []

        # Create canvas and initialize image for drawing
        self.canvas = tk.Canvas(self.root, width=1000, height=550, bg="white")
        self.canvas.pack(pady=20)
        self.image = Image.new("RGBA", (1000, 550), (255, 255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)

        # Toolbar Frame
        self.toolbar_frame = tk.Frame(self.root, bg="#444444")
        self.toolbar_frame.pack(fill=tk.X, pady=10)

        # Brush Color Picker
        self.color_button = tk.Button(self.toolbar_frame, text="Brush Color", command=self.choose_color, bg="#6c757d", fg="white", relief="flat")
        self.color_button.pack(side=tk.LEFT, padx=10)

        # Brush Size Slider
        self.size_slider = tk.Scale(self.toolbar_frame, from_=1, to=30, orient=tk.HORIZONTAL, label="Brush Size", bg="#444444", fg="white", sliderlength=25)
        self.size_slider.set(self.brush_size)
        self.size_slider.pack(side=tk.LEFT, padx=10)

        # Brush Opacity Slider
        self.opacity_slider = tk.Scale(self.toolbar_frame, from_=0, to=255, orient=tk.HORIZONTAL, label="Brush Opacity", bg="#444444", fg="white", sliderlength=25)
        self.opacity_slider.set(self.brush_opacity)
        self.opacity_slider.pack(side=tk.LEFT, padx=10)

        # Undo and Redo Buttons
        self.undo_button = tk.Button(self.toolbar_frame, text="Undo", command=self.undo, bg="#6c757d", fg="white", relief="flat")
        self.undo_button.pack(side=tk.LEFT, padx=10)
        self.redo_button = tk.Button(self.toolbar_frame, text="Redo", command=self.redo, bg="#6c757d", fg="white", relief="flat")
        self.redo_button.pack(side=tk.LEFT, padx=10)

        # Clear Button
        self.clear_button = tk.Button(self.toolbar_frame, text="Clear", command=self.clear_canvas, bg="#e74c3c", fg="white", relief="flat")
        self.clear_button.pack(side=tk.LEFT, padx=10)

        # Save Button
        self.save_button = tk.Button(self.toolbar_frame, text="Save", command=self.save_image, bg="#28a745", fg="white", relief="flat")
        self.save_button.pack(side=tk.LEFT, padx=10)

        # Mouse Events
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw_on_canvas)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Choose Brush Color")[1]
        if color_code:
            self.brush_color = color_code

    def start_draw(self, event):
        self.drawing = True
        self.last_x, self.last_y = event.x, event.y

    def draw_on_canvas(self, event):
        if self.drawing:
            # Smooth the drawing with anti-aliasing or interpolation
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                    width=self.brush_size, fill=self.brush_color, capstyle=tk.ROUND, smooth=True)
            self.draw.line([self.last_x, self.last_y, event.x, event.y], fill=self.brush_color, width=self.brush_size)
            self.last_x, self.last_y = event.x, event.y

    def stop_draw(self, event):
        self.drawing = False
        self.last_x, self.last_y = None, None
        self.save_history()

    def save_history(self):
        # Save the current state into history for undo/redo
        self.history.append(self.image.copy())
        self.redo_history.clear()
        self.update_buttons()

    def undo(self):
        if self.history:
            self.redo_history.append(self.image.copy())
            self.image = self.history.pop()
            self.draw = ImageDraw.Draw(self.image)
            self.update_canvas()
            self.update_buttons()

    def redo(self):
        if self.redo_history:
            self.history.append(self.image.copy())
            self.image = self.redo_history.pop()
            self.draw = ImageDraw.Draw(self.image)
            self.update_canvas()
            self.update_buttons()

    def clear_canvas(self):
        self.image = Image.new("RGBA", (1000, 550), (255, 255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)
        self.canvas.delete("all")
        self.history.clear()
        self.redo_history.clear()
        self.update_buttons()

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
        if file_path:
            self.image.save(file_path)
            messagebox.showinfo("Image Saved", f"Image saved at {file_path}")

    def update_canvas(self):
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.tk_image, anchor=tk.NW)

    def update_buttons(self):
        if self.history:
            self.undo_button.config(state=tk.NORMAL)
        else:
            self.undo_button.config(state=tk.DISABLED)

        if self.redo_history:
            self.redo_button.config(state=tk.NORMAL)
        else:
            self.redo_button.config(state=tk.DISABLED)


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ModernDrawingApp(root)
    root.mainloop()
import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from PIL import Image, ImageDraw, ImageTk


class VisuallyAppealingDrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visually Appealing Drawing App")
        self.root.geometry("1000x650")
        self.root.config(bg="#2c3e50")

        # Customizable Brush
        self.drawing = False
        self.last_x, self.last_y = None, None
        self.brush_color = "#ffffff"
        self.brush_size = 5
        self.brush_opacity = 255
        self.history = []
        self.redo_history = []

        # Create canvas and initialize image for drawing
        self.canvas = tk.Canvas(self.root, width=1000, height=550, bg="#ecf0f1", bd=0, highlightthickness=0)
        self.canvas.pack(pady=20)
        self.image = Image.new("RGBA", (1000, 550), (255, 255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)

        # Toolbar Frame
        self.toolbar_frame = tk.Frame(self.root, bg="#34495e", bd=0)
        self.toolbar_frame.pack(fill=tk.X, pady=10)

        # Brush Color Picker Button
        self.color_button = self.create_button(self.toolbar_frame, "Brush Color", self.choose_color, "#1abc9c")
        self.color_button.pack(side=tk.LEFT, padx=10)

        # Brush Size Slider
        self.size_slider = tk.Scale(self.toolbar_frame, from_=1, to=30, orient=tk.HORIZONTAL, label="Brush Size",
                                    bg="#34495e", fg="white", sliderlength=25, font=("Helvetica", 10))
        self.size_slider.set(self.brush_size)
        self.size_slider.pack(side=tk.LEFT, padx=10)

        # Brush Opacity Slider
        self.opacity_slider = tk.Scale(self.toolbar_frame, from_=0, to=255, orient=tk.HORIZONTAL, label="Brush Opacity",
                                       bg="#34495e", fg="white", sliderlength=25, font=("Helvetica", 10))
        self.opacity_slider.set(self.brush_opacity)
        self.opacity_slider.pack(side=tk.LEFT, padx=10)

        # Undo and Redo Buttons
        self.undo_button = self.create_button(self.toolbar_frame, "Undo", self.undo, "#e74c3c")
        self.undo_button.pack(side=tk.LEFT, padx=10)
        self.redo_button = self.create_button(self.toolbar_frame, "Redo", self.redo, "#f39c12")
        self.redo_button.pack(side=tk.LEFT, padx=10)

        # Clear Button
        self.clear_button = self.create_button(self.toolbar_frame, "Clear", self.clear_canvas, "#e74c3c")
        self.clear_button.pack(side=tk.LEFT, padx=10)

        # Save Button
        self.save_button = self.create_button(self.toolbar_frame, "Save", self.save_image, "#28a745")
        self.save_button.pack(side=tk.LEFT, padx=10)

        # Mouse Events
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw_on_canvas)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

    def create_button(self, parent, text, command, color):
        button = tk.Button(parent, text=text, command=command, font=("Helvetica", 12), fg="white", relief="flat",
                           bg=color, bd=0)
        button.bind("<Enter>", self.on_hover_in)
        button.bind("<Leave>", self.on_hover_out)
        button.config(activebackground=color, activeforeground="white")
        return button

    def on_hover_in(self, event):
        event.widget.config(bg="#16a085")

    def on_hover_out(self, event):
        event.widget.config(bg="#1abc9c")

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Choose Brush Color")[1]
        if color_code:
            self.brush_color = color_code

    def start_draw(self, event):
        self.drawing = True
        self.last_x, self.last_y = event.x, event.y

    def draw_on_canvas(self, event):
        if self.drawing:
            # Smooth the drawing with anti-aliasing or interpolation
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                    width=self.brush_size, fill=self.brush_color, capstyle=tk.ROUND, smooth=True)
            self.draw.line([self.last_x, self.last_y, event.x, event.y], fill=self.brush_color, width=self.brush_size)
            self.last_x, self.last_y = event.x, event.y

    def stop_draw(self, event):
        self.drawing = False
        self.last_x, self.last_y = None, None
        self.save_history()

    def save_history(self):
        # Save the current state into history for undo/redo
        self.history.append(self.image.copy())
        self.redo_history.clear()
        self.update_buttons()

    def undo(self):
        if self.history:
            self.redo_history.append(self.image.copy())
            self.image = self.history.pop()
            self.draw = ImageDraw.Draw(self.image)
            self.update_canvas()
            self.update_buttons()

    def redo(self):
        if self.redo_history:
            self.history.append(self.image.copy())
            self.image = self.redo_history.pop()
            self.draw = ImageDraw.Draw(self.image)
            self.update_canvas()
            self.update_buttons()

    def clear_canvas(self):
        self.image = Image.new("RGBA", (1000, 550), (255, 255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)
        self.canvas.delete("all")
        self.history.clear()
        self.redo_history.clear()
        self.update_buttons()

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
        if file_path:
            self.image.save(file_path)
            messagebox.showinfo("Image Saved", f"Image saved at {file_path}")

    def update_canvas(self):
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.tk_image, anchor=tk.NW)

    def update_buttons(self):
        if self.history:
            self.undo_button.config(state=tk.NORMAL)
        else:
            self.undo_button.config(state=tk.DISABLED)

        if self.redo_history:
            self.redo_button.config(state=tk.NORMAL)
        else:
            self.redo_button.config(state=tk.DISABLED)


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = VisuallyAppealingDrawingApp(root)
    root.mainloop()
