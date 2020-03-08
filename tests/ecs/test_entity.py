import unittest
from pong.ecs.entity import Entity


class TestEntity(unittest.TestCase):
    def test_count(self):
        self.assertEqual(Entity.count, 0)
        _e = Entity()
        self.assertEqual(Entity.count, 1)
