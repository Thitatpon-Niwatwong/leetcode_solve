class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        max_substring = 0
        substring = set()
        for right in range(len(s)):
            while s[right] in substring:
                substring.remove(s[left])
                left += 1
            substring.add(s[right])
            max_substring = max(max_substring, right-left+1)
        return max_substring


x = Solution()
s = "bbbbb"
print(x.lengthOfLongestSubstring(s))
