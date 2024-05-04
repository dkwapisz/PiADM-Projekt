import tkinter as tk

import numpy as np

from Utils.TriangleMesh import TriangleMesh
from Visualizers.MayaviVisualizer import MayaviVisualizer
from Visualizers.Open3DVisualizer import Open3DVisualizer
from Visualizers.VTKVisualizer import VTKVisualizer


class MainGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Mesh Visualization")
        self.master.geometry("300x200")
        self.master.configure(bg="#f0f0f0")

        self.label = tk.Label(self.master, text="Choose visualization library:", bg="#f0f0f0", font=("Arial", 12))
        self.label.pack(pady=10)

        self.choices = ["Mayavi", "VTK", "Open3D"]
        self.choice_var = tk.StringVar()
        self.choice_var.set("Mayavi")

        self.dropdown = tk.OptionMenu(self.master, self.choice_var, *self.choices)
        self.dropdown.config(font=("Arial", 10))
        self.dropdown.pack(pady=5)

        self.button_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.button_frame.pack(pady=10)

        self.visualize_button = tk.Button(self.button_frame, text="Visualize", command=self.visualize, bg="#4CAF50",
                                          fg="white", font=("Arial", 12), padx=10, pady=5)
        self.visualize_button.pack(side=tk.LEFT, padx=5)

        self.quit_button = tk.Button(self.button_frame, text="Quit", command=self.master.quit, bg="#f44336", fg="white",
                                     font=("Arial", 12), padx=10, pady=5)
        self.quit_button.pack(side=tk.RIGHT, padx=5)

    def visualize(self):
        choice = self.choice_var.get()

        points = np.random.rand(100, 3)
        triangles = np.random.randint(0, 100, (200, 3))
        mesh = TriangleMesh(points, triangles)

        if choice == "Mayavi":
            mayavi_visualizer = MayaviVisualizer(mesh)
            mayavi_visualizer.visualize()
        elif choice == "VTK":
            vtk_visualizer = VTKVisualizer(mesh)
            vtk_visualizer.visualize()
        elif choice == "Open3D":
            open3d_visualizer = Open3DVisualizer(mesh)
            open3d_visualizer.visualize()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainGUI(root)
    root.mainloop()
