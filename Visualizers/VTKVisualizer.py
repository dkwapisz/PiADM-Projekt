import vtk


class VTKVisualizerBasic:
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
        render_window.SetSize(1200, 800)
        render_window.AddRenderer(renderer)

        interactor = vtk.vtkRenderWindowInteractor()
        interactor.SetRenderWindow(render_window)

        render_window.Render()
        interactor.Start()


class VTKVisualizerDetailed:
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

        triangle_normals = vtk.vtkPolyDataNormals()
        triangle_normals.SetInputData(polydata)
        triangle_normals.ComputeCellNormalsOn()
        triangle_normals.ComputePointNormalsOff()
        triangle_normals.Update()

        heights = vtk.vtkDoubleArray()
        heights.SetName("Heights")
        for point in self.mesh.points:
            heights.InsertNextValue(point[2])
        polydata.GetPointData().SetScalars(heights)

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(polydata)
        mapper.SetScalarRange(polydata.GetPointData().GetScalars().GetRange())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        renderer = vtk.vtkRenderer()
        renderer.AddActor(actor)

        render_window = vtk.vtkRenderWindow()
        render_window.SetSize(1200, 800)
        render_window.AddRenderer(renderer)

        interactor = vtk.vtkRenderWindowInteractor()
        interactor.SetRenderWindow(render_window)

        style = vtk.vtkInteractorStyleTrackballCamera()
        interactor.SetInteractorStyle(style)

        render_window.Render()
        interactor.Start()
