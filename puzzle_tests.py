#
# Tests for sliding block puzzles
#

import pytest
from slider_puzzle import SliderPuzzle
from slider_search import SliderSearch

class TestSliderPuzzle:

    def test_generation(self):
        sp = SliderPuzzle(3)
        for i, x in enumerate(sp.puzzle):
            assert i == x

    def test_block_location(self):
        sp = SliderPuzzle(4)
        assert sp.current_block_location(15) == (3, 3)
        assert sp.current_block_location(0) == (0, 0)

        sp = SliderPuzzle(3, [8, 1, 2, 7, 4, 5, 6, 3, 0 ])
        assert sp.current_block_location(8) == (0, 0)
        assert sp.current_block_location(0) == (2, 2)
        assert sp.current_block_location(7) == (1, 0)
        assert sp.current_block_location(3) == (2, 1)

    def test_swap_state(self):
        sp = SliderPuzzle(3)
        swapped_sp = sp.swapped_state(0,8)
        assert swapped_sp[0] == 8
        assert swapped_sp[-1] == 0

    def test_possible_states(self):
        sp = SliderPuzzle(3)
        pm = sp.possible_moves()
        assert len(pm) == 2
        assert pm[0] == [ 1, 0, 2, 3, 4, 5, 6, 7, 8 ]
        assert pm[1] == [ 3, 1, 2, 0, 4, 5, 6, 7, 8 ]
        
        sp.puzzle = sp.swapped_state(0, 4)
        pm = sp.possible_moves()
        assert len(pm) == 4

class TestSliderSearch:

    def test_constructor(self):
        ss = SliderSearch(4)
        assert len(ss.puzzle.puzzle) == 16
        ss = SliderSearch(3)
        assert len(ss.puzzle.puzzle) == 9

    def test_goal_state(self):
        ss = SliderSearch(4)
        expected_goal_state = [x for x in xrange(16)]
        assert ss.goal_state() == expected_goal_state

    def test_heuristics(self):
        ss = SliderSearch(3)
        assert ss.heuristic_misplaced(ss.puzzle.puzzle) == 0
        assert ss.heuristic_manhatten_distance(ss.puzzle.puzzle) == 0
        
        ss = SliderSearch(3, [3, 1, 2, 0, 4, 5, 6, 7, 8])
        assert ss.heuristic_misplaced(ss.puzzle.puzzle) == 2
        assert ss.heuristic_manhatten_distance(ss.puzzle.puzzle) == 2

        ss = SliderSearch(3, [8, 1, 2, 3, 4, 5, 6, 7, 0])
        assert ss.heuristic_misplaced(ss.puzzle.puzzle) == 2
        assert ss.heuristic_manhatten_distance(ss.puzzle.puzzle) == 8
        

    def test_a_star_search(self):
        ss = SliderSearch(3)
        res = ss.search_a_star()
        exp = [[0,1,2,3,4,5,6,7,8]]
        assert res == exp

        ss = SliderSearch(3, [1,0,2,3,4,5,6,7,8])
        res = ss.search_a_star()
        exp = [[1,0,2,3,4,5,6,7,8],[0,1,2,3,4,5,6,7,8]]
