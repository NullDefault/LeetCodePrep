"""
~Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
~In Pascal's triangle, each number is the sum of the two numbers directly above it.
~Example:

    Input: 5
    Output:
    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]
"""


class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        if num_rows == 0:
            return []

        def make_row(row_above):

            n = len(row_above)
            new_row = [None] * (n + 1)

            new_row[0], new_row[-1] = row_above[0], row_above[-1]

            for i in range(1, len(new_row) - 1):
                left = row_above[i - 1]
                right = row_above[i]
                new_row[i] = left + right

            return new_row

        triangle = [[1]]
        for r in range(1, num_rows):
            triangle.append(make_row(triangle[r - 1]))
        return triangle
