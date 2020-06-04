"""
~You are given an n x n 2D matrix representing an image.

~Rotate the image by 90 degrees (clockwise).

~Note:

    ~You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
     DO NOT allocate another 2D matrix and do the rotation.
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for row in range(0, n//2):
            for col in range(row, n-row-1):
                # store current cell in temp variable
                temp = matrix[row][col]
                # move values from left to top
                matrix[row][col] = matrix[n-1-col][row]
                # move values form bottom to left
                matrix[n-1-col][row] = matrix[n-1-row][n-1-col]
                # move values from right to bottom
                matrix[n-1-row][n-1-col] = matrix[col][n-1-row]
                # assing temp to right
                matrix[col][n-1-row] = temp