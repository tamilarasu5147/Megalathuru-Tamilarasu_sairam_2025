'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
'''
#logic1
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        ways = [0] * (n + 1)
        ways[1] = 1
        ways[2] = 2

        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]

        return ways[n]
    
#logic2
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        prev1, prev2 = 1, 2

        for i in range(3, n + 1):
            current = prev1 + prev2
            prev1, prev2 = prev2, current

        return prev2