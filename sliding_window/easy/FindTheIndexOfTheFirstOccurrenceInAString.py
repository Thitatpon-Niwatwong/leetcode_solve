class Solution(object):
    def strStr(self, haystack, needle):
        h = len(haystack)
        n = len(needle)
        for i in range(h - n + 1):
            j = 0
            while j < n and haystack[j + i] == needle[j]:
                j += 1
            if j == n:
                return i
        return -1

