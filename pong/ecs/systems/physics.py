from typing import List
from . import System
from pong.ecs import World
from pong.ecs.components import Position, Velocity


class Physics(System):
    def __init__(self) -> None:
        pass

    def step(self, world: World, dt: int):
        for e in world.get_entities_with_components(['position', 'velocity']):
            position: Position = e.get_component('position')
            velocity: Velocity = e.get_component('velocity')

            position.x += velocity.x
            position.y += velocity.y
