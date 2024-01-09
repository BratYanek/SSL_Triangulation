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
        self.distance_label = ttk.Label(master=self.master, text='Odległości pomiędzy źródłem dźwięku a wyznaczonym średnim punktem:', font='Calibri 12')
        self.distance_label.pack()
        self.distance_label = ttk.Label(master=self.master, text='Odległość bezwzględna: N/A m', font='Calibri 12')
        self.distance_label.pack()
        self.distance_x_label = ttk.Label(master=self.master, text='Odległość względem osi X: N/A m', font='Calibri 12')
        self.distance_x_label.pack()
        self.distance_y_label = ttk.Label(master=self.master, text='Odległość względem osi Y: N/A m', font='Calibri 12')
        self.distance_y_label.pack()
        self.distance_z_label = ttk.Label(master=self.master, text='Odległość względem osi Z: N/A m', font='Calibri 12')
        self.distance_z_label.pack()

        # Figure with larger size
        self.fig = matplotlib.figure.Figure(figsize=(6, 6))
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

            max_x_distance = np.ptp(x)
            max_y_distance = np.ptp(y)
            max_z_distance = np.ptp(z)

            print(max_x_distance, max_y_distance, max_z_distance)

            xa = np.mean(x)
            ya = np.mean(y)
            za = np.mean(z)

            xs = 0
            ys = -1.1
            zs = 1.65

            distance = np.sqrt(((xs-xa)**2)+((ys-ya)**2)+((zs-za)**2))
            distance_x = np.sqrt((xs-xa)**2)
            distance_y = np.sqrt((ys-ya)**2)
            distance_z = np.sqrt((zs-za)**2)
            self.distance_label.config(text=f'Odległość bezwględna: {distance:.2f} m')
            self.distance_x_label.config(text=f'Odległość względem osi X: {distance_x:.2f} m')
            self.distance_y_label.config(text=f'Odległość względem osi Y: {distance_y:.2f} m')
            self.distance_z_label.config(text=f'Odległość względem osi Z: {distance_z:.2f} m')

            self.ax.scatter(1, 1, 0.5, c='red', marker='s', label='węzeł_1', s=50)
            self.ax.scatter(-1, 1, 0.5, c='red', marker='s', label='węzeł_2', s=50)
            self.ax.scatter(xs, ys, zs, c='green', marker='o', label='żródło dźwięku', s=300)
            self.ax.scatter(x, y, z, c='blue', marker='o', label='punkty_pomiarowe')
            self.ax.scatter(xa, ya, za, c='magenta', marker='o', label='średni punkt', s=300)

            self.ax.plot([1, 1], [1, 1], [0.5, 0], color='black', linestyle='-', linewidth=2)
            self.ax.plot([-1, -1], [1, 1], [0.5, 0], color='black', linestyle='-', linewidth=2)

            # Adjust axis scaling
            self.ax.set_xlim([-1.5, 1.5])
            self.ax.set_ylim([-2.5, 1.5])
            self.ax.set_zlim([0, 2.5])


            self.ax.legend()  # Show legend with labels

            self.canvas.draw()

def main():
    root = tk.Tk()
    app = MultilateracjaApp(root)
    root.mainloop()

main()
