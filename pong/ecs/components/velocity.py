from . import Component


class Velocity(Component):
    def __init__(self, x: int = 0, y: int = 0) -> None:
        super().__init__('velocity')
        self.x = x
        self.y = y
