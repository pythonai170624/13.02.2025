# adapter_3d_to_2d/d2_nice_painter.py
from .d2_painter import D2Painter

class D2NicePainter(D2Painter):
    def paint_2d_shape(self, shape):
        print(f"Printing nicely {shape}")
