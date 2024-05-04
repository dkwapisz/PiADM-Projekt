from mayavi import mlab


class MayaviVisualizer:
    def __init__(self, mesh):
        self.mesh = mesh

    def visualize(self):
        mlab.triangular_mesh(self.mesh.points[:, 0], self.mesh.points[:, 1], self.mesh.points[:, 2],
                             self.mesh.triangles)
        mlab.show()
