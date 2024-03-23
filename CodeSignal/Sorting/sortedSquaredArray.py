"""
Note: Come up with a linear solution, since that is what you would be asked to do in an interview.

You have a sorted array of integers. Write a function that returns a sorted array containing the squares of those integers.

Example

For array = [-6, -4, 1, 2, 3, 5], the output should be
solution(array) = [1, 4, 9, 16, 25, 36].

The array of squared integers from array is: [36, 16, 1, 4, 9, 25]. When sorted, it becomes: [1, 4, 9, 16, 25, 36].
"""

def solution(array):
    # Get the length of the array
    n = len(array)
    # Initialize two pointers: left and right
    left, right = 0, n - 1
    # Initialize an array to store the squared numbers
    result = [0] * n
    
    # Iterate until the left pointer meets or exceeds the right pointer
    while left <= right:
        # Calculate the square of the number at the left pointer
        left_sq = array[left] ** 2
        # Calculate the square of the number at the right pointer
        right_sq = array[right] ** 2
        
        # Compare the squared numbers
        if left_sq > right_sq:
            # If the square of the number at the left pointer is greater, 
            # assign it to the result array and move the left pointer to the right
            result[right - left] = left_sq
            left += 1
        else:
            # If the square of the number at the right pointer is greater or equal, 
            # assign it to the result array and move the right pointer to the left
            result[right - left] = right_sq
            right -= 1
    
    # Return the array of squared numbers
    return result
