'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''
#logic1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complement_dict:
                return [complement_dict[complement], i]
            complement_dict[num] = i
            
#logic 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_index = [(num, i) for i, num in enumerate(nums)]
        nums_with_index.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = nums_with_index[left][0] + nums_with_index[right][0]
            if current_sum == target:
                return [nums_with_index[left][1], nums_with_index[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1