from typing import List
from pong.ecs import World


class System:
    def __init__(self) -> None:
        raise NotImplementedError()

    def step(self, world: World, dt: int):
        raise NotImplementedError()
