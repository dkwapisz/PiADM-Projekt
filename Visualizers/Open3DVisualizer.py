import numpy as np
import open3d as o3d


class Open3DVisualizerBasic:
    def __init__(self, mesh):
        self.mesh = mesh

    def visualize(self):
        mesh_o3d = o3d.geometry.TriangleMesh()
        mesh_o3d.vertices = o3d.utility.Vector3dVector(self.mesh.points)
        mesh_o3d.triangles = o3d.utility.Vector3iVector(self.mesh.triangles)

        vis = o3d.visualization.Visualizer()
        vis.create_window(width=1200, height=800)
        vis.add_geometry(mesh_o3d)
        vis.run()
        vis.destroy_window()


class Open3DVisualizerDetailed:
    def __init__(self, mesh):
        self.mesh = mesh

    def visualize(self):
        mesh_o3d = o3d.geometry.TriangleMesh()
        mesh_o3d.vertices = o3d.utility.Vector3dVector(self.mesh.points)
        mesh_o3d.triangles = o3d.utility.Vector3iVector(self.mesh.triangles)
        mesh_o3d.compute_vertex_normals()

        colors = np.zeros_like(self.mesh.points)
        heights = self.mesh.points[:, 2]
        normalized_heights = (heights - np.min(heights)) / (np.max(heights) - np.min(heights))

        colors[:, 0] = normalized_heights
        colors[:, 1] = 1 - normalized_heights

        mesh_o3d.vertex_colors = o3d.utility.Vector3dVector(colors)

        lines = o3d.geometry.LineSet.create_from_triangle_mesh(mesh_o3d)
        lines.paint_uniform_color([0.0, 0.0, 0.0])

        axis = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.5)

        vis = o3d.visualization.Visualizer()
        vis.create_window(width=1200, height=800)
        vis.add_geometry(mesh_o3d)
        vis.add_geometry(lines)
        vis.add_geometry(axis)

        vis.run()
        vis.destroy_window()
