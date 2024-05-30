'''
73. Set Matrix Zeroes
Medium

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False
        colZero = False

        # Determine if the first row or first column need to be zero
        for r in range(rows):
            if matrix[r][0] == 0:
                colZero = True
                break
        
        for c in range(cols):
            if matrix[0][c] == 0:
                rowZero = True
                break

        # Use first row and first column to mark zeros
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        # Zero out cells based on the marks in the first row and column
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # Zero out the first row if needed
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0
        
        # Zero out the first column if needed
        if colZero:
            for r in range(rows):
                matrix[r][0] = 0