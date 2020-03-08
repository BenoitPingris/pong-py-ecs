import sys
from pong.ecs import World, Entity
from pong.ecs.components import Position, Velocity
from pong.ecs.systems import Physics


def main():
    w = World()

    e = w.create_entity()
    e.add_component(Position())
    e.add_component(Velocity(1,1))
    w.add_system(Physics())
    print(e.get_component('position').x)
    print(e.get_component('position').y)
    w.step(0)
    print(e.get_component('position').x)
    print(e.get_component('position').y)
    return 0


if __name__ == "__main__":
    sys.exit(main())
