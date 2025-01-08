from math import gcd
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        gcd_length = gcd(len(str1),len(str2))
        return str1[:gcd_length]

x = Solution()
str1 = "ABC"
str2 = "ABC"
print(x.gcdOfStrings(str1,str2))
