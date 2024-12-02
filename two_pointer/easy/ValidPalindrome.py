class Solution:
    def isPalindrome(self, s):
        s = ""
        for i in s:
            if i.isalnum():
                s += i.lower()
        left = 0
        right = len(s)-1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


x = Solution()
s = "A man, a plan, a canal: Panama"
print(x.isPalindrome(s))
