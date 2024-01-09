import tkinter as tk
from tkinter import ttk, filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
import matplotlib.figure

class MultilateracjaApp:
    def __init__(self, master):
        self.master = master
        master.title('Triangulacja')
        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = ttk.Label(master=self.master, text='Współrzędne ŚNP', font='Calibri 18 bold')
        title_label.pack()

        # Figure with larger size
        self.fig = matplotlib.figure.Figure(figsize=(10, 8))
        self.ax = self.fig.add_subplot(projection='3d')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2Tk(self.canvas, self.master)
        toolbar.update()
        toolbar.pack(anchor="w", fill=tk.X)

        # Button and file selection
        tk.Button(self.master, text='Wybierz plik', command=self.select_file).pack(pady=10)
        tk.Button(self.master, text='Wyświetl dane', command=self.plot).pack(pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename(title='Wybierz plik', filetypes=[('Text Files', '*.txt')])
        if file_path:
            self.file_path = file_path

    def load_data(self):
        try:
            data = np.loadtxt(fname=self.file_path, delimiter=' ')
            x = data[:, 0]
            y = data[:, 1]
            z = data[:, 2]
            return x, y, z
        except (IOError, ValueError) as e:
            print(f"Error loading data: {e}")
            return None

    def plot(self):
        if not hasattr(self, 'file_path'):
            print("Please select a file first.")
            return

        self.ax.clear()
        data = self.load_data()
        if data:
            x, y, z = data
            self.ax.scatter(1, 1, 0.5, c='red', marker='o')
            self.ax.scatter(0, 1, 0.5, c='red', marker='o')
            self.ax.scatter(0, -1.3, 1.65, c='green', marker='o', label='sound source')
            self.ax.scatter(x, y, z, c='blue', marker='o')

            # Adjust axis scaling
            self.ax.set_xlim([-3, 3])
            self.ax.set_ylim([-3, 3])
            self.ax.set_zlim([0, 3])

            self.canvas.draw()

def main():
    root = tk.Tk()
    app = MultilateracjaApp(root)
    root.mainloop()

main()
