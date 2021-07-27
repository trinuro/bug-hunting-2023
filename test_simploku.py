
__copyright__ = "Copyright (C) 2021 The University of Manchester"


from unittest import TestCase
from nose.tools import assert_equals, assert_in, assert_raises

from simploku import SimplokuPuzzle, SolutionNotFoundError, InvalidPuzzleError


def check_contains_exactly(actual_contents, expected_contents):
    assert_equals(sorted(actual_contents), expected_contents)


def assert_puzzle_solution_is(puzzle, solution):
    puzzle = SimplokuPuzzle(puzzle)
    assert_equals(puzzle.solution(), solution)


def assert_puzzle_solution_is_one_of(puzzle, *solutions):
    puzzle = SimplokuPuzzle(puzzle)
    assert_in(puzzle.solution(), solutions)


def assert_no_solution_exists(puzzle):
    puzzle = SimplokuPuzzle(puzzle)
    with assert_raises(SolutionNotFoundError):
        puzzle.solution()


def assert_puzzle_is_invalid(puzzle):
    with assert_raises(InvalidPuzzleError):
        puzzle = SimplokuPuzzle(puzzle)


class SimplokuTest(TestCase):

    def test_return_a_solved_one_by_one_puzzle_unchanged(self):
        puzzle_to_solve = [[1]]
        assert_puzzle_solution_is(puzzle_to_solve, puzzle_to_solve)

    def should_return_a_solved_two_by_two_puzzle_unchanged(self):
        puzzle_to_solve = [[1, 2], [2, 1]]
        assert_puzzle_solution_is(puzzle_to_solve, puzzle_to_solve)

    def should_solve_a_two_by_two_puzzle_with_1_gap_top_left(self):
        assert_puzzle_solution_is([[None, 1],
                                   [1,    2]],
                                  [[2, 1],
                                   [1, 2]])

    def should_solve_a_different_two_by_two_puzzle_with_1_gap_top_left(self):
        assert_puzzle_solution_is([[None, 2],
                                   [2, 1]],
                                  [[1, 2],
                                   [2, 1]])

    def should_solve_a_two_by_two_puzzle_with_1_gap_top_right(self):
        assert_puzzle_solution_is([[1, None],
                                   [2, 1]],
                                  [[1, 2],
                                   [2, 1]])

    def should_solve_a_two_by_two_puzzle_with_1_gap_bottom_left(self):
        assert_puzzle_solution_is([[1, 2],
                                   [None, 1]],
                                  [[1, 2],
                                   [2, 1]])

    def should_solve_a_two_by_two_puzzle_with_1_gap_bottom_right(self):
        assert_puzzle_solution_is([[1, 2],
                                   [2, None]],
                                  [[1, 2],
                                   [2, 1]])

    def should_solve_a_three_by_three_puzzle_with_1_gap_top_left(self):
        assert_puzzle_solution_is([[None, 2, 3],
                                   [2,    3, 1],
                                   [3,    1, 2]],
                                  [[1, 2, 3],
                                   [2, 3, 1],
                                   [3, 1, 2]])

    def should_solve_a_different_three_by_three_puzzle_with_1_gap_top_left(self):
        assert_puzzle_solution_is([[None, 3, 1],
                                   [3, 1, 2],
                                   [1, 2, 3]],
                                  [[2, 3, 1],
                                   [3, 1, 2],
                                   [1, 2, 3]])

    def should_solve_a_different_three_by_three_puzzle_with_1_gap_in_the_centre(self):
        assert_puzzle_solution_is([[2, 3,    1],
                                   [3, None, 2],
                                   [1, 2,    3]],
                                  [[2, 3, 1],
                                   [3, 1, 2],
                                   [1, 2, 3]])

    def should_solve_a_nine_by_nine_puzzle_with_4_gaps(self):
        assert_puzzle_solution_is([[None, 2, 3,    4, 5, 6,    7, 8, 9],
                                   [2,    3, 4,    5, 6, 7,    8, 9, 1],
                                   [3,    4, 5,    6, 7, None, 9, 1, 2],
                                   [4,    5, 6,    7, 8, 9,    1, 2, 3],
                                   [5,    6, 7,    8, 9, 1,    2, 3, 4],
                                   [6,    7, 8,    9, 1, 2,    3, 4, 5],
                                   [7,    8, None, 1, 2, None, 4, 5, 6],
                                   [8,    9, 1,    2, 3, 4,    5, 6, 7],
                                   [9, 1, 2, 3,    4, 5, 6, 7, 8]],
                                  [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                   [2, 3, 4, 5, 6, 7, 8, 9, 1],
                                   [3, 4, 5, 6, 7, 8, 9, 1, 2],
                                   [4, 5, 6, 7, 8, 9, 1, 2, 3],
                                   [5, 6, 7, 8, 9, 1, 2, 3, 4],
                                   [6, 7, 8, 9, 1, 2, 3, 4, 5],
                                   [7, 8, 9, 1, 2, 3, 4, 5, 6],
                                   [8, 9, 1, 2, 3, 4, 5, 6, 7],
                                   [9, 1, 2, 3, 4, 5, 6, 7, 8]])

    def should_solve_a_nine_by_nine_puzzle_with_7_gaps(self):
        assert_puzzle_solution_is([[None, 2, 3,    4, 5, None, 7, 8, 9],
                                   [2,    3, 4,    5, 6, 7,    8, 9, 1],
                                   [3,    4, 5,    6, 7, None, 9, 1, None],
                                   [4,    5, 6,    7, 8, 9,    1, 2, 3],
                                   [5,    6, 7,    8, 9, 1,    2, 3, 4],
                                   [6,    7, 8,    9, 1, 2,    3, 4, 5],
                                   [7,    8, None, 1, 2, None, 4, 5, None],
                                   [8,    9, 1,    2, 3, 4,    5, 6, 7],
                                   [9,    1, 2,    3, 4, 5,    6, 7, 8]],
                                  [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                   [2, 3, 4, 5, 6, 7, 8, 9, 1],
                                   [3, 4, 5, 6, 7, 8, 9, 1, 2],
                                   [4, 5, 6, 7, 8, 9, 1, 2, 3],
                                   [5, 6, 7, 8, 9, 1, 2, 3, 4],
                                   [6, 7, 8, 9, 1, 2, 3, 4, 5],
                                   [7, 8, 9, 1, 2, 3, 4, 5, 6],
                                   [8, 9, 1, 2, 3, 4, 5, 6, 7],
                                   [9, 1, 2, 3, 4, 5, 6, 7, 8]])

    def should_find_a_3_by_3_solution_when_more_than_one_exists(self):
        assert_puzzle_solution_is_one_of([[None, None, 3],
                                          [None, None, 2],
                                          [None, None, 1]],
                                         [[1, 2, 3],
                                          [3, 1, 2],
                                          [2, 3, 1]],
                                         [[2, 1, 3],
                                          [1, 3, 2],
                                          [3, 2, 1]])

    def should_find_a_4_by_4_solution_when_more_than_one_exists(self):
        assert_puzzle_solution_is_one_of([[None, None, 3, 4],
                                          [None, None, 4, 3],
                                          [3,    4,    1, 2],
                                          [4,    3,    2, 1]],
                                         [[1, 2, 3, 4],
                                          [2, 1, 4, 3],
                                          [3, 4, 1, 2],
                                          [4, 3, 2, 1]],
                                         [[2, 1, 3, 4],
                                          [1, 2, 4, 3],
                                          [3, 4, 1, 2],
                                          [4, 3, 2, 1]])

    def should_reject_an_impossible_puzzle(self):
        assert_no_solution_exists([[None, None, 3],
                                   [None, None, 2],
                                   [1,    None, None]])

    def should_reject_a_rectangular_puzzle(self):
        assert_puzzle_is_invalid([[None, 2,    3,    4],
                                  [2,    None, None, None]])

    def should_reject_an_impossible_puzzle(self):
        assert_no_solution_exists([[None, 3,    3],
                                   [None, None, None],
                                   [None, None, None]])

