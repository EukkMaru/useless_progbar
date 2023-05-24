import tkinter as tk
from tkinter import ttk
import time

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("what the fuck")

        # Create a style for the progressbar
        self.style = ttk.Style()
        self.style.theme_use('default')

        self.colors = ['#66DE93', '#4D88FF', '#F0B849', '#F0497D']
        self.color_index = 0

        self.style.configure("TProgressbar", thickness=50, 
                             background=self.colors[self.color_index % len(self.colors)], 
                             troughcolor=self.colors[(self.color_index - 1) % len(self.colors)])

        self.progress = ttk.Progressbar(self, length=500, mode='determinate', style="TProgressbar")
        self.progress.pack(padx=20, pady=20)  # padx option adds horizontal padding

        self.progress_time = 120  # Total time for progress bar to complete one cycle in seconds
        self.fps = 24  # Frame rate
        self.delay_time = round(1000 / self.fps)  # Delay between updates in milliseconds
        self.increment = 100 / (self.progress_time * self.fps)  # Increment amount

        self.update_progress()

    def update_progress(self):
        self.progress['value'] += self.increment
        if self.progress['value'] >= 100:
            self.progress['value'] = 0
            self.color_index += 1
            self.style.configure("TProgressbar", 
                                 background=self.colors[self.color_index % len(self.colors)], 
                                 troughcolor=self.colors[(self.color_index - 1) % len(self.colors)])
        self.after(self.delay_time, self.update_progress)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
