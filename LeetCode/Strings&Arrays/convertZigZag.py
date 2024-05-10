'''
6. Zigzag Conversion
Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If there's only one row or numRows is greater than or equal to the length of s,
        # then the string remains the same, no zigzag pattern can be formed.
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize a list of empty strings, one for each row in the zigzag pattern.
        res = [''] * numRows
        
        # Initialize index to keep track of the current row, and step to control the direction of movement.
        index, step = 0, 1

        # Iterate through each character in the input string s.
        for char in s:
            # Append the character to the corresponding row in the result list.
            res[index] += char
            
            # Check if we've reached the top row.
            if index == 0:
                # If so, change the step to downward movement.
                step = 1
            # Check if we've reached the bottom row.
            elif index == numRows - 1:
                # If so, change the step to upward movement.
                step = -1
            
            # Update the index to move to the next row.
            index += step

        # Join the strings in the result list to form the zigzag pattern.
        return ''.join(res)