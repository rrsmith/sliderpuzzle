#
# Solving the slider puzzles using search
#


class SliderPuzzle(object):
    """
    Represents a sliding block puzzle
    of arbitrary square size
    """

    def __init__(self, square_size=3, puzzle=None):
        self.square_size = square_size

        if puzzle is not None:
            self.puzzle = puzzle
        else:
            self.puzzle = self.generate_random_puzzle(self.square_size)

    def current_block_location(self, block_number, state=None):
        """
        Gets the current block location
        as a tuple (rowindex, columnindex)
        """
        if state is None:
            state = self.puzzle

        block_index = state.index(block_number)
        return (block_index // self.square_size, block_index % self.square_size)

    def generate_random_puzzle(self, square_size=3):
        """
        Generates a random puzzle of given square size
        """
        new_puzzle = [x for x in xrange(square_size**2)]
        return new_puzzle

    def swapped_state(self, index_a, index_b):
        """
        Generates a copy of the puzzle with two blocks swapped
        Note that this does NOT check for or guarantee validity
        """
        swapped = [x for x in self.puzzle]
        swapped[index_a], swapped[index_b] = swapped[index_b], swapped[index_a]
        return swapped

    def possible_moves(self):
        """
        Generates the set of possible states available
        from the current puzzle
        """
        possible_states = []
        empty_index = self.puzzle.index(0)

        if ((empty_index % self.square_size) + 1) < self.square_size:
            possible_states.append(self.swapped_state(empty_index, empty_index+1))
        if ((empty_index % self.square_size - 1) >= 0):
            possible_states.append(self.swapped_state(empty_index, empty_index-1))

        if (empty_index + self.square_size) < len(self.puzzle):
            possible_states.append(self.swapped_state(empty_index, empty_index+self.square_size))
        if (empty_index - self.square_size) >= 0:
            possible_states.append(self.swapped_state(empty_index, empty_index-self.square_size))

        return possible_states