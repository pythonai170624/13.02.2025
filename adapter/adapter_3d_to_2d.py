# adapter_3d_to_2d/adapter_3d_to_2d.py
from .d3_painter import D3Painter
from .d2_nice_painter import D2NicePainter

class Adapter3Dto2D(D3Painter):
    def __init__(self):
        self.d2_nice_painter = D2NicePainter()

    def paint_3d_shape(self, shape):
        for d2_shape in shape.get_d2_shapes():  # adapt
            self.d2_nice_painter.paint_2d_shape(d2_shape)
