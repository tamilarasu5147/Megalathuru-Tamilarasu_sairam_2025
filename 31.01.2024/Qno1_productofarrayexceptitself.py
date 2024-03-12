'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
'''
#logic 1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        left_product = 1
        for i in range(n):
            result[i] *= left_product
            left_product *= nums[i]
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        return result
    
#logic 2
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        left_product, right_product = 1, 1
        
        for i in range(n):
            result[i] *= left_product
            result[n - 1 - i] *= right_product
            left_product *= nums[i]
            right_product *= nums[n - 1 - i]
        
        return result