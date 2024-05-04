import open3d as o3d


class Open3DVisualizer:
    def __init__(self, mesh):
        self.mesh = mesh

    def visualize(self):
        mesh_o3d = o3d.geometry.TriangleMesh()
        mesh_o3d.vertices = o3d.utility.Vector3dVector(self.mesh.points)
        mesh_o3d.triangles = o3d.utility.Vector3iVector(self.mesh.triangles)
        o3d.visualization.draw_geometries([mesh_o3d])
