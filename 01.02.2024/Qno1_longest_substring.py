'''
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''
#logic1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        start = 0
        max_length = 0

        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1

            char_index[s[end]] = end
            max_length = max(max_length, end - start + 1)

        return max_length
    
#logic2
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        start = 0
        max_length = 0

        for end in range(len(s)):
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1

            char_set.add(s[end])
            max_length = max(max_length, end - start + 1)

        return max_length