import open3d as o3d


class Open3DVisualizer:
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