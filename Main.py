import sys
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox

from Utils.MeshGenerator import RandomMeshGenerator, FileMeshGenerator
from Utils.Validation import validate_file_format
from Visualizers.MatplotlibVisualizer import MatplotlibVisualizer
from Visualizers.MayaviVisualizer import MayaviVisualizer
from Visualizers.Open3DVisualizer import Open3DVisualizerBasic, Open3DVisualizerDetailed
from Visualizers.PlotlyVisualizer import PlotlyVisualizer
from Visualizers.VTKVisualizer import VTKVisualizerBasic, VTKVisualizerDetailed


class MainGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Mesh Visualization")
        self.master.geometry("600x400")
        self.master.configure(bg="#f0f0f0")

        self.label = tk.Label(self.master, text="Choose visualization library:", bg="#f0f0f0", font=("Arial", 12))
        self.label.pack(pady=10)

        self.choices = ["Mayavi", "VTK - Basic", "VTK - Detailed", "Open3D - Basic", "Open3D - Detailed", "Matplotlib",
                        "Plotly"]
        self.choice_var = tk.StringVar()
        self.choice_var.set("Mayavi")

        self.dropdown = tk.OptionMenu(self.master, self.choice_var, *self.choices)
        self.dropdown.config(font=("Arial", 10))
        self.dropdown.pack(pady=5)

        self.mode_var = tk.StringVar()
        self.mode_var.set("random")
        self.mode_var.trace('w', self.update_mode)

        self.random_mode_radio = tk.Radiobutton(self.master, text="Random Mesh", variable=self.mode_var, value="random")
        self.random_mode_radio.pack(pady=5)

        self.num_points_entry = tk.Entry(self.master)
        self.num_points_entry.pack(pady=5)
        self.num_points_entry.insert(0, "100")

        self.num_triangles_entry = tk.Entry(self.master)
        self.num_triangles_entry.pack(pady=5)
        self.num_triangles_entry.insert(0, "200")

        self.file_mode_radio = tk.Radiobutton(self.master, text="Mesh from File", variable=self.mode_var, value="file")
        self.file_mode_radio.pack(pady=5)

        self.file_path_label = tk.Label(self.master, text="")
        self.file_path_label.pack(pady=5)

        self.choose_file_button = tk.Button(self.master, text="Choose file", command=self.choose_file)
        self.choose_file_button.pack(pady=5)

        self.button_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.button_frame.pack(pady=10)

        self.visualize_button = tk.Button(self.button_frame, text="Visualize", command=self.visualize, bg="#4CAF50",
                                          fg="white", font=("Arial", 12), padx=10, pady=5)
        self.visualize_button.pack(side=tk.LEFT, padx=5)

        self.quit_button = tk.Button(self.button_frame, text="Quit", command=self.quit_program, bg="#f44336",
                                     fg="white",
                                     font=("Arial", 12), padx=10, pady=5)
        self.quit_button.pack(side=tk.RIGHT, padx=5)

        self.master.protocol("WM_DELETE_WINDOW", self.quit_program)

        self.update_mode()

    def update_mode(self, *args):
        if self.mode_var.get() == "random":
            self.choose_file_button.config(state="disabled")
            self.num_points_entry.config(state="normal")
            self.num_triangles_entry.config(state="normal")
        else:
            self.choose_file_button.config(state="normal")
            self.num_points_entry.config(state="disabled")
            self.num_triangles_entry.config(state="disabled")

    def choose_file(self):
        file_path = tk.filedialog.askopenfilename()
        if file_path:
            choice = self.choice_var.get()
            if validate_file_format(file_path, choice):
                self.file_path_label.config(text=file_path)

    def visualize(self):
        choice = self.choice_var.get()

        if self.mode_var.get() == "random":
            num_points = int(self.num_points_entry.get())
            num_triangles = int(self.num_triangles_entry.get())
            generator = RandomMeshGenerator(num_points, num_triangles)
        else:
            file_path = self.file_path_label.cget("text")
            if not file_path:
                tk.messagebox.showerror("Error", "Please choose")
                return
            generator = FileMeshGenerator(file_path)

        mesh = generator.generate()

        self.master.withdraw()

        if choice == "Mayavi":
            visualizer = MayaviVisualizer(mesh)
        elif choice == "VTK - Basic":
            visualizer = VTKVisualizerBasic(mesh)
        elif choice == "VTK - Detailed":
            visualizer = VTKVisualizerDetailed(mesh)
        elif choice == "Open3D - Basic":
            visualizer = Open3DVisualizerBasic(mesh)
        elif choice == "Open3D - Detailed":
            visualizer = Open3DVisualizerDetailed(mesh)
        elif choice == "Matplotlib":
            visualizer = MatplotlibVisualizer(mesh)
        elif choice == "Plotly":
            visualizer = PlotlyVisualizer(mesh)
        else:
            visualizer = None

        visualizer.visualize()
        self.master.deiconify()

    def quit_program(self):
        self.master.quit()
        sys.exit(0)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainGUI(root)
    root.mainloop()
