from pong.ecs.entity import Entity
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from pong.ecs.systems.system import System


class World:
    def __init__(self) -> None:
        self.systems: List['System'] = []
        self.entities: List[Entity] = []
        self.last_time = 0

    def step(self, ts: int) -> None:
        dt = ts - self.last_time
        self.last_time = ts
        for system in self.systems:
            system.step(self, dt)

    def create_entity(self) -> Entity:
        ent = Entity()
        self.entities.append(ent)
        return ent

    def add_system(self, system: 'System') -> 'System':
        self.systems.append(system)
        return system

    def get_entities_with_components(self, comp_names: List[str]) -> List[Entity]:
        entities: List[Entity] = []

        for e in self.entities:
            if e.has_components(comp_names):
                entities.append(e)
        return entities
