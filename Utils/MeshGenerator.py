from abc import ABC, abstractmethod

import numpy as np
import open3d as o3d


class TriangleMesh:
    def __init__(self, points, triangles):
        self.points = points
        self.triangles = triangles


class MeshGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class RandomMeshGenerator(MeshGenerator):
    def __init__(self, num_points, num_triangles):
        self.num_points = num_points
        self.num_triangles = num_triangles

    def generate(self):
        points = np.random.rand(self.num_points, 3)
        triangles = np.random.randint(0, self.num_points, (self.num_triangles, 3))
        return TriangleMesh(points, triangles)


class FileMeshGenerator(MeshGenerator):
    def __init__(self, file_path):
        self.file_path = file_path

    def generate(self):
        mesh_o3d = o3d.io.read_triangle_mesh(self.file_path)
        points = np.asarray(mesh_o3d.vertices)
        triangles = np.asarray(mesh_o3d.triangles)
        return TriangleMesh(points, triangles)
