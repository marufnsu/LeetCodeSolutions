"""
DIFFICULTY LEVEL: HARD
You have an array nums. We determine two functions to perform on nums. In both cases, n is the length of nums:

fi(nums) = nums[0] · nums[1] · ... · nums[i - 1] · nums[i + 1] · ... · nums[n - 1]. (In other words, fi(nums) is the product of all array elements except the ithf.)
g(nums) = f0(nums) + f1(nums) + ... + fn-1(nums).
Using these two functions, calculate all values of f modulo the given m. Take these new values and add them together to get g. You should return the value of g modulo the given m.

Example
For nums = [1, 2, 3, 4] and m = 12, the output should be
solution(nums, m) = 2.

The array of the values of f is: [24, 12, 8, 6]. If we take all the elements modulo m, we get:
[0, 0, 8, 6]. The sum of those values is 8 + 6 = 14, making the answer 14 % 12 = 2.
"""

def solution(nums, m):
    # Initialize variables s (sum) and p (product) to 0 and 1 respectively
    s, p = 0, 1
    
    # Iterate through each number in the input array nums
    for num in nums:
        # Update s and p using the current number
        # s is updated by adding the product of the current number and the previous product value, then taking modulo m
        # p is updated by multiplying the previous product value and the current number, then taking modulo m
        s, p = (p + s * num) % m, (p * num) % m
    
    # Return the final value of s
    return s


"""
Explanation:

We initialize two variables, s (sum) and p (product), to 0 and 1 respectively. These variables will keep track of the accumulated sum and product as we iterate through the array nums.
We iterate through each number num in the array nums.
Inside the loop, we update the values of s and p using the current number num:
    For s, we add the product of the previous p and the current num to the previous s, then take modulo m. This represents the sum of the current product and the accumulated sum so far.
    For p, we multiply the previous p by the current num, then take modulo m. This represents the product of the previous product and the current number.
After iterating through all numbers in nums, we return the final value of s, which represents the sum of the products modulo m. This is the result of the function.
"""