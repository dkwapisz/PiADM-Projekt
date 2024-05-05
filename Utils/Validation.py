import os
import tkinter.messagebox


def validate_file_format(file_path, choice):
    file_extension = os.path.splitext(file_path)[1]

    if choice in ["Mayavi", "VTK", "Matplotlib", "Plotly"] and file_extension not in [".vtk", ".vtp", ".ply", ".stl",
                                                                                      ".obj"]:
        tkinter.messagebox.showerror("Error", f"Invalid file format for {choice}. Please choose a .vtk, "
                                              ".vtp, .ply, .stl, or .obj file.")
        return False
    elif choice == "Open3D" and file_extension not in [".ply", ".stl", ".obj", ".off", ".gltf", ".glb"]:
        tkinter.messagebox.showerror("Error", "Invalid file format for Open3D. Please choose a .ply, "
                                              ".stl, .obj, .off, .gltf, or .glb file.")
        return False

    return True
