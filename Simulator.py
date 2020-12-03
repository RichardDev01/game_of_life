from World import *
import copy


class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.


    1.Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    2.Any live cell with two or three live neighbours lives on to the next generation.
    3.Any live cell with more than three live neighbours dies, as if by overpopulation.
    4.Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

    """

    def __init__(self, world = None):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        if world == None:
            self.world = World(20)
        else:
            self.world = world

    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """

        # copy.deepcopy()

        #Copy current state of the world for processing
        world_init = copy.deepcopy(self.world)

        self.world.height

        for x in range(self.world.width):
            for y in range(self.world.height):
                neighbour_count = np.count_nonzero(world_init.get_neighbours(x, y))

                status_count = world_init.get(x,y)

                #print(neighbour_count,status_count)

                # #rule 1
                # if neighbour_count < 2:
                #     self.world.set(x, y, 0)

                #rule 2
                if neighbour_count == 2 or neighbour_count == 3:
                    self.world.set(x, y, 1)
                else:
                    self.world.set(x, y, 0)



        self.generation += 1
        return self.world

    def get_generation(self):
        """
        Returns the value of the current generation of the simulated Game of Life.

        :return: generation of simulated Game of Life.
        """
        return self.generation

    def get_world(self):
        """
        Returns the current version of the ``World``.

        :return: current state of the world.
        """
        return self.world

    def set_world(self, world: World) -> None:
        """
        Changes the current world to the given value.

        :param world: new version of the world.

        """
        self.world = world