# adapter_3d_to_2d/d3_nice_painter.py
from .d3_painter import D3Painter

class D3NicePainter(D3Painter):
    def paint_3d_shape(self, shape):
        print(f"D3 is printing not so nice... {shape}")
