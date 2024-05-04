import vtk


class VTKVisualizer:
    def __init__(self, mesh):
        self.mesh = mesh

    def visualize(self):
        points = vtk.vtkPoints()
        for point in self.mesh.points:
            points.InsertNextPoint(point)

        triangles = vtk.vtkCellArray()
        for triangle in self.mesh.triangles:
            vtk_triangle = vtk.vtkTriangle()
            vtk_triangle.GetPointIds().SetId(0, triangle[0])
            vtk_triangle.GetPointIds().SetId(1, triangle[1])
            vtk_triangle.GetPointIds().SetId(2, triangle[2])
            triangles.InsertNextCell(vtk_triangle)

        polydata = vtk.vtkPolyData()
        polydata.SetPoints(points)
        polydata.SetPolys(triangles)

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(polydata)

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        renderer = vtk.vtkRenderer()
        renderer.AddActor(actor)

        render_window = vtk.vtkRenderWindow()
        render_window.AddRenderer(renderer)

        interactor = vtk.vtkRenderWindowInteractor()
        interactor.SetRenderWindow(render_window)

        render_window.Render()
        interactor.Start()
