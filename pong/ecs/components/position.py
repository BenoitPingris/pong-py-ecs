from . import Component


class Position(Component):
    def __init__(self, x: int = 0, y: int = 0) -> None:
        super().__init__('position')
        self.x = x
        self.y = y
