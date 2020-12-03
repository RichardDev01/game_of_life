from unittest import TestCase
from Simulator import *


class TestSimulator(TestCase):
    """
    Tests for ``Simulator`` implementation.
    """
    def setUp(self):
        self.sim = Simulator()

    def test_update(self):
        """
        Tests that the update functions returns an object of World type.
        """
        self.assertIsInstance(self.sim.update(), World)

    def test_get_generation(self):
        """
        Tests whether get_generation returns the correct value:
            - Generation should be 0 when Simulator just created;
            - Generation should be 2 after 2 updates.
        """
        self.assertIs(self.sim.generation, self.sim.get_generation())
        self.assertEqual(self.sim.get_generation(), 0)
        self.sim.update()
        self.sim.update()
        self.assertEqual(self.sim.get_generation(), 2)

    def test_get_world(self):
        """
        Tests whether the object passed when get_world() is called is of World type, and has the required dimensions.
        When no argument passed to construction of Simulator, world is square shaped with size 20.
        """
        self.assertIs(self.sim.world, self.sim.get_world())
        self.assertEqual(self.sim.get_world().width, 20)
        self.assertEqual(self.sim.get_world().height, 20)

    def test_set_world(self):
        """
        Tests functionality of set_world function.
        """
        world = World(10)
        self.sim.set_world(world)
        self.assertIsInstance(self.sim.get_world(), World)
        self.assertIs(self.sim.get_world(), world)

    # def test_world_cords(self):
    #
    #     self.sim.update()
    #     self.assertEqual(self.sim.world.get(0,0),1)
    #
    # def test_check_neighbours(self):
    #     self.sim.world.set(0,1)
    #     self.assertEqual(np.count_nonzero(self.sim.world.get_neighbours(1, 1)), 1)

    def test_rule1_underpopulation(self):
        # 1.Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        self.sim.world.set(5, 4, 1)
        self.sim.world.set(5, 5, 1)
        self.sim.world.set(5, 6, 1)

        self.sim.update()

        self.assertEqual(self.sim.world.get(5, 4), 0)
        self.assertEqual(self.sim.world.get(5, 5), 1)
        self.assertEqual(self.sim.world.get(5, 6), 0)

    def test_rule2_survive(self):
        # 2.Any live cell with two or three live neighbours lives on to the next generation.
        self.sim.world.set(2, 1, 1)
        self.sim.world.set(2, 2, 1)
        self.sim.world.set(2, 3, 1)
        self.sim.world.set(1, 2, 1)
        self.sim.world.set(3, 2, 1)

        self.sim.update()
        self.assertEqual(self.sim.world.get(2, 2), 0)



