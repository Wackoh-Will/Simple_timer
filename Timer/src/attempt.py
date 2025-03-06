import tkinter as tk
import time


class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer")
        self.root.geometry("500x150")

        self.start_time = 0
        self.running = False

        self.label = tk.Label(root, text="Press Enter to Start", font=("Arial", 30))
        self.label.pack(pady=20)

        self.update_timer()

        self.root.bind("<Return>", self.toggle_timer) # REMEMBER this is how to bind 

    def toggle_timer(self, event=None):
        if self.running:
            self.running = False
        else:
            self.start_time = time.time() - (self.start_time or 0)
            self.running = True
            self.update_timer()

    def update_timer(self):
        if self.running:
            passed_time = time.time() - self.start_time
            minutes, seconds = divmod(passed_time, 60)
            milli = int((seconds % 1) * 100)
            self.label.config(text=f"{int(minutes)}:{int(seconds):02}.{milli:02}")

        self.root.after(50, self.update_timer)



root = tk.Tk()
app = TimerApp(root)
root.mainloop()