"""
~Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    ~Each row must contain the digits 1-9 without repetition.
    ~Each column must contain the digits 1-9 without repetition.
    ~Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

"""


################### ORIGINAL SOLUTION ##################################################################################


class SudokuSet:
    def __init__(self):
        self.cells = {1: 0,
                      2: 0,
                      3: 0,
                      4: 0,
                      5: 0,
                      6: 0,
                      7: 0,
                      8: 0,
                      9: 0}

    def count_val(self, val):
        if val == ".":
            return True
        val = int(val)
        if self.cells[val] == 0:
            self.cells[val] += 1
            return True

        else:
            return False


def make_data_dict():
    return {
        0: SudokuSet(),
        1: SudokuSet(),
        2: SudokuSet(),
        3: SudokuSet(),
        4: SudokuSet(),
        5: SudokuSet(),
        6: SudokuSet(),
        7: SudokuSet(),
        8: SudokuSet(),
    }


def get_square(row, col):
    squares = [[0, 1, 2],
               [3, 4, 5],
               [6, 7, 8]]
    return squares[row // 3][col // 3]


def is_valid_sudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    rows = make_data_dict()  # 0-8 rows
    cols = make_data_dict()  # 0-8 cols
    sqrs = make_data_dict()  # 0 1 2
    # 3 4 5
    # 6 7 8  <- The Squares of the Sudoku Board
    for row in range(0, 9):
        for col in range(0, 9):
            a = rows[row].count_val(board[row][col])
            b = cols[col].count_val(board[row][col])
            c = sqrs[get_square(row, col)].count_val(board[row][col])
            if not a or not b or not c:
                return False
    return True
#######################################################################################################################

################### IMPROVED SOLUTION ##################################################################################


def is_valid_sudoku_improved(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """

    def check_rows():
        for r in range(0, 9):
            row = board[r]
            s = set()
            nums = []
            for e in row:
                if e == ".":
                    continue
                else:
                    e = int(e)
                    s.add(e)
                    nums.append(e)
            if len(s) != len(nums):
                return False
        return True

    def check_cols():
        for c in range(0, 9):
            col = []
            for r in range(0, 9):
                col.append(board[r][c])

            s = set()
            nums = []
            for e in col:
                if e == ".":
                    continue
                else:
                    e = int(e)
                    s.add(e)
                    nums.append(e)
            if len(s) != len(nums):
                return False
        return True

    def check_sqs():
        for sq_r in range(0, 9, 3):
            for sq_c in range(0, 9, 3):
                s = set()
                nums = []
                for r in range(0, 3):
                    for c in range(0, 3):
                        t_r = sq_r + r
                        t_c = sq_c + c
                        e = board[t_r][t_c]
                        if e == ".":
                            continue
                        else:
                            e = int(e)
                            s.add(e)
                            nums.append(e)
                if len(s) != len(nums):
                    return False
        return True

    return check_rows() and check_cols() and check_sqs()


