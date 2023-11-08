# A simple Sudoku-type puzzle solver

__copyright__ = "Copyright (C) 2021 The University of Manchester"

import copy


class SolutionNotFoundError(Exception):
    """Exception raised when a solution to the input puzzle cannot be found."""
    pass



class SimplokuPuzzle(object):
    """A simple Sudoku-style puzzle representation and solver."""
    input_puzzle = []

    def __init__(self, puzzle_to_solve):
        self.input_puzzle = puzzle_to_solve
        self.puzzle_size = len(self.input_puzzle)
        self.rows = list(range(0, self.puzzle_size))
        self.columns = self.rows

        self.expected_values = list(range(1, self.puzzle_size+1))
        self.puzzle_places = [(r, c) for r in self.rows for c in self.columns]

    def solution(self):
        return self.find_solution(self.input_puzzle)

    def missing_values(self, puzzle, place):
        (row, col) = place

        row_values = [rmv for rmv in self.expected_values if rmv not in puzzle[row]]
        column_values = [cmv for cmv in self.expected_values if not any(r[col] == cmv for r in puzzle)]
        return [mv for mv in row_values if mv in column_values]

    def find_solution(self, puzzle_to_solve):
        # Find the places in the puzzle where there is a missing value
        empty_places = [(r, c) for (r, c) in self.puzzle_places if puzzle_to_solve[r][c] is None]

        if len(empty_places) == 0:
            # The puzzle is already solved, and can be returned as the solution
            return puzzle_to_solve

        # Otherwise, we have some work to do

        # Find the possible values that could be put into each empty place in the puzzle
        candidate_values = {place: self.missing_values(puzzle_to_solve, place) for place in empty_places}

        # If there are any empty places with no candidate values, then the puzzle does not have a solution
        if any(len(candidate_values[p]) == 0 for p in empty_places):
            raise SolutionNotFoundError()

        # Otherwise, look for empty places which have only one possible value.
        # Add that value to the puzzle, and then try to solve the remaining empty places.
        places_to_solve_first = [place for place in empty_places if len(candidate_values[place]) == 1]
        if len(places_to_solve_first) > 0:
            (row, col) = places_to_solve_first[0]
            puzzle_to_solve[row][col] = candidate_values[(row, col)][0]
            return self.find_solution(puzzle_to_solve)

        # Otherwise, the empty cells all have more than one candidate value.  We just have to try these values
        # in turn until we find one that works.  If none of them work then the puzzle is unsolvable.
        # We know there will always be at least one such place if we reach this point (unless there is a bug in the code).
        places_to_solve_next = [place for place in empty_places if len(candidate_values[place]) > 1]
        if len(places_to_solve_next) > 0:
            # Try placing each candidate value in turn and then solving the resulting problem.
            (row, col) = places_to_solve_next[0]
            for candidate in candidate_values[(row, col)]:
                try:
                    # Make a copy of the puzzle we are trying to solve so we can try out a possible solution without
                    # damaging the original puzzle, in case we need to go back and try again.
                    puzzle = copy.deepcopy(puzzle_to_solve)
                    puzzle[row][col] = candidate
                    return self.find_solution(puzzle)
                except SolutionNotFoundError:
                    # If the current candidate value didn't lead to a solution, then try the next one.
                    continue

        # If we reach this point, then something weird has happened and we were not able to find a solution.
        raise SolutionNotFoundError()


def main():
    puzzle_start_state = [[None, 2, 3, 4,    5, 6,    7,    8, 9],
                          [2,    3, 4, 5,    6, 7,    8,    9, 1],
                          [3,    4, 5, None, 7, None, 9,    1, 2],
                          [4,    5, 6, 7,    8, 9,    1,    2, 3],
                          [5,    6, 7, 8,    9, 1,    2,    3, 4],
                          [6,    7, 8, 9,    1, 2,    3,    4, 5],
                          [7,    8, 9, None, 2, None, 4,    5, 6],
                          [8,    9, 1, 2,    3, 4,    5,    6, 7],
                          [None, 1, 2, None, 4, 5,    None, 7, 8]]
    puzzle = SimplokuPuzzle(puzzle_start_state)
    print(puzzle.solution())


if __name__ == "__main__":
    main()
