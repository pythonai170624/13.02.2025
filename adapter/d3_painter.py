# adapter_3d_to_2d/d3_painter.py
from abc import ABC, abstractmethod

class D3Painter(ABC):
    @abstractmethod
    def paint_3d_shape(self, shape):
        pass
