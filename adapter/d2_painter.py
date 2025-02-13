# adapter_3d_to_2d/d2_painter.py
from abc import ABC, abstractmethod

class D2Painter(ABC):
    @abstractmethod
    def paint_2d_shape(self, shape):
        pass
