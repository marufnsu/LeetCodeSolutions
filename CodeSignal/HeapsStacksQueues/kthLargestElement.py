'''
Note: Avoid using built-in std::nth_element (or analogous built-in functions in languages other than C++) when solving this challenge. 
Implement them yourself, since this is what you would be asked to do during a real interview.

Find the kth largest element in an unsorted array. This will be the kth largest element in sorted order, not the kth distinct element.

Example
For nums = [7, 6, 5, 4, 3, 2, 1] and k = 2, the output should be
solution(nums, k) = 6;
For nums = [99, 99] and k = 1, the output should be
solution(nums, k) = 99.
'''

import heapq

def solution(nums, k):
    # Create a min heap of the first k elements of nums
    h = nums[:k]
    heapq.heapify(h)
    
    # For each element after the first k elements
    for x in nums[k:]:
        # Push the current element onto the heap and pop the smallest element off the heap
        heapq.heappushpop(h, x)
    
    # Return the smallest element in the heap, which is the kth largest element in nums
    return h[0]