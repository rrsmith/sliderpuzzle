#
# Search slider puzzles for best path
#

import math
from slider_puzzle import SliderPuzzle


class SliderSearch(object):
    """
    Represents a searcher on SliderPuzzles
    """
    def __init__(self, square_size=3, puzzle=None):
        self.square_size = square_size
        self.goal_block_location = self.in_order_goal_block_location
        self.goal_state = self.in_order_goal_state
        self.frontier = []

        self.puzzle = SliderPuzzle(self.square_size, puzzle)

    def in_order_goal_block_location(self, block_number):
        """
        Gets the goal block location
        as a tuple (rowindex, columnindex)
        Assumes goal state is all values in order
        """
        return (block_number // self.square_size,
                block_number % self.square_size)

    def in_order_goal_state(self):
        """
        Gets the goal state for the puzzle
        when goal is all values in order
        """
        return [x for x in xrange(self.square_size**2)]

    def heuristic_misplaced(self, state):
        """
        Gets the heuristic value for the given state
        using a simple count of misplaced blocks
        """
        misplaced = 0
        for x in self.puzzle.puzzle:
            if self.goal_block_location(x) != self.puzzle.current_block_location(x, state):
                misplaced += 1
        return misplaced

    def heuristic_manhatten_distance(self, state):
        """
        Gets the heuristic value for the given state
        using manhatten distance
        """
        m_distances = [abs((self.puzzle.current_block_location(x, state)[0]
                            - self.goal_block_location(x)[0])
                        + (self.puzzle.current_block_location(x, state)[1]
                            - self.goal_block_location(x)[1]))
                        for x in self.puzzle.puzzle]
        return sum(m_distances)
