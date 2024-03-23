"""
You have an unsorted array arr of non-negative integers and a number s. 
Find a longest contiguous subarray in arr that has a sum equal to s. 
Return two integers that represent its inclusive bounds. If there are several possible answers, 
return the one with the smallest left bound. If there are no answers, return [-1].

Your answer should be 1-based, meaning that the first position of the array is 1 instead of 0.

Example
For s = 12 and arr = [1, 2, 3, 7, 5], the output should be
solution(s, arr) = [2, 4].

The sum of elements from the 2nd position to the 4th position (1-based) is equal to 12: 2 + 3 + 7.

For s = 15 and arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], the output should be
solution(s, arr) = [1, 5].

The sum of elements from the 1st position to the 5th position (1-based) is equal to 15: 1 + 2 + 3 + 4 + 5.

For s = 15 and arr = [1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10], the output should be
solution(s, arr) = [1, 8].

The sum of elements from the 1st position to the 8th position (1-based) is equal to 15: 1 + 2 + 3 + 4 + 5 + 0 + 0 + 0.
"""

def solution(s, arr):
    left = 0  # Initialize left pointer
    curr_sum = 0  # Initialize current sum
    max_len = 0  # Initialize maximum length of subarray
    result = [-1]  # Initialize result list with default value

    # Iterate through the array with right pointer
    for right in range(len(arr)):
        # Update current sum by adding the current element
        curr_sum += arr[right]

        # Shrink the window if the sum exceeds s
        while curr_sum > s:
            curr_sum -= arr[left]
            left += 1

        # Check if the current subarray is longer than the previous longest subarray
        if curr_sum == s and right - left + 1 > max_len:
            max_len = right - left + 1
            # Update result with the bounds of the longest subarray
            result = [left + 1, right + 1]  # Adjust indices to be 1-based

    return result

"""
Explanation:

We initialize left pointer at index 0, curr_sum to 0, max_len to 0, and result list with a default value of [-1].
We iterate through the array using the right pointer.
At each step, we add the current element to curr_sum.
We then shrink the window by moving the left pointer if the sum exceeds s.
If the current sum equals s and the length of the current subarray is greater than the previous longest subarray, we update max_len and result.
Finally, we return the result, which represents the inclusive bounds of the longest subarray with sum s.
"""