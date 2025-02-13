# adapter_3d_to_2d/d3_shape.py
from .d2_shape import D2Shape

class D3Shape:
    def __init__(self):
        self.shapes = []

    def get_d2_shapes(self):
        return self.shapes

    def add_d2_shape(self, shape):
        if isinstance(shape, D2Shape):
            self.shapes.append(shape)

    def __str__(self):
        return "3D Shape containing 2D Shapes"
