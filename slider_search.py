#
# Search slider puzzles for best path
#

import math
from slider_puzzle import SliderPuzzle
from collections import deque


class SliderSearch(object):
    """
    Represents a searcher on SliderPuzzles
    """
    def __init__(self, square_size=3, puzzle=None):
        self.square_size = square_size
        self.goal_block_location = self.in_order_goal_block_location
        self.goal_state = self.in_order_goal_state
        self.heuristic = self.heuristic_manhatten_distance

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

    def search_a_star(self):
        """
        Find best path solution using A*
        Returns the list of states from initial to goal
        or None if no solution possible
        """
        frontier = deque([Node(self.puzzle.puzzle, None, 0)])
        explored = set()
        goal = self.goal_state()

        while 1:
            if not frontier:
                return None
            else:
                # choose node
                costs = [self.heuristic(x.state) + x.path_cost for x in frontier]
                selected_index = costs.index(min(costs))
                selected = frontier[selected_index]
                if (selected.state == goal):
                    path = []
                    while selected.parent is not None:
                        path.append(selected.state)
                        selected = selected.parent
                    path.append(selected.state)
                    path = path[::-1]
                    return path
                else:
                    # Expand the node
                    self.puzzle.puzzle = selected.state
                    ps = self.puzzle.possible_moves()
                    for x in ps:
                        if str(x) not in explored:
                            frontier.append(Node(x, selected, selected.path_cost+1))
                    # Move checked into explored
                    ss = str(selected.state)
                    explored.add(ss)
                    frontier.remove(selected)


class Node(object):
    def __init__(self, state, parent, path_cost):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost
