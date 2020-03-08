from pong.ecs.components import Component
import time
from typing import Dict, List, Union


class Entity:
    count = 0

    def __init__(self) -> None:
        self.id = f'{time.time_ns()}{Entity.count}'
        self.components: Dict[str, Component] = {}
        Entity.count += 1

    def add_component(self, comp: Component) -> 'Entity':
        self.components[comp.name] = comp
        return self

    def get_component(self, comp_name: str) -> Union[None, Component]:
        try:
            return self.components[comp_name]
        except:
            return None

    def get_components(self, comp_names: List[str]) -> List[Component]:
        comps: List[Component] = []
        for name in comp_names:
            c = self.get_component(name)
            if c:
                comps.append(c)
        return comps

    def has_component(self, comp_name: str) -> bool:
        return comp_name in self.components

    def has_components(self, comp_names: List[str]) -> bool:
        return all(name in self.components for name in comp_names)
