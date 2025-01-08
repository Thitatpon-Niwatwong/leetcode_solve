class Solution(object):
    def reverseString(self, s):
        reversed_s = []
        left = 0
        right = len(s) - 1
        while left <= right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1

x = Solution()
s = ["h","e","l","l","o"]
print(x.reverseString(s))