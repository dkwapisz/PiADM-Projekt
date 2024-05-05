import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np


class MatplotlibVisualizer:
    def __init__(self, mesh):
        self.mesh = mesh

    def visualize(self):
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')

        x = self.mesh.points[:, 0]
        y = self.mesh.points[:, 1]
        z = self.mesh.points[:, 2]

        triangles = tri.Triangulation(x, y, self.mesh.triangles)

        ax.plot_trisurf(triangles, z, cmap=plt.cm.CMRmap)

        ax.set_box_aspect([np.ptp(x), np.ptp(y), np.ptp(z)])

        plt.show()
