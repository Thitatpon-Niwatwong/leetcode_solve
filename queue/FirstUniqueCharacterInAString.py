class Solution(object):
    def firstUniqChar(self, s):
        all_char = dict()
        for char in s:
            if char in all_char:
                all_char[char] += 1
            else:
                all_char[char] = 1
        for i,char in enumerate(s):
            if all_char[char] == 1:
                return i
        return -1

x = Solution()
print(x.firstUniqChar("aabb"))

