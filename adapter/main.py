# adapter_3d_to_2d/main.py
from adapter.d3_shape import D3Shape
from adapter.d2_shape import D2Shape
from adapter.adapter_3d_to_2d import Adapter3Dto2D

def draw(painter, shape):
    painter.paint_3d_shape(shape)

if __name__ == "__main__":
    d3_shape = D3Shape()
    d3_shape.add_d2_shape(D2Shape())  # Adding a 2D shape to the 3D shape

    draw(Adapter3Dto2D(), d3_shape)
