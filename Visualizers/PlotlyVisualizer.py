import numpy as np
import plotly.graph_objects as go


class PlotlyVisualizer:
    def __init__(self, mesh):
        self.mesh = mesh

    def visualize(self):
        scale_factor = 0.01

        x = self.mesh.points[:, 0] * scale_factor
        y = self.mesh.points[:, 1] * scale_factor
        z = self.mesh.points[:, 2] * scale_factor

        fig = go.Figure(data=[
            go.Mesh3d(
                x=x,
                y=y,
                z=z,
                i=self.mesh.triangles[:, 0],
                j=self.mesh.triangles[:, 1],
                k=self.mesh.triangles[:, 2],
                color='lightpink',
                opacity=0.50
            )
        ])

        max_range = np.array([x.ptp(), y.ptp(), z.ptp()]).max() * 0.5

        mid_x = (x.max() + x.min()) * 0.5
        mid_y = (y.max() + y.min()) * 0.5
        mid_z = (z.max() + z.min()) * 0.5
        x_eye = mid_x + max_range
        y_eye = mid_y + max_range
        z_eye = mid_z + max_range

        fig.update_layout(
            width=1200,
            height=800,
            autosize=False,
            scene=dict(
                aspectratio=dict(
                    x=np.ptp(x),
                    y=np.ptp(y),
                    z=np.ptp(z)
                ),
                aspectmode='manual',
                camera=dict(
                    eye=dict(x=x_eye, y=y_eye, z=z_eye)
                )
            )
        )

        fig.show()
