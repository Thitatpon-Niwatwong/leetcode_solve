class Solution(object):
    def characterReplacement(self, s, k):
        all_char = dict()
        max_length = 0
        left = 0
        for right in range(len(s)):
            if s[right] in all_char:
                all_char[s[right]] += 1
            else:
                all_char[s[right]] = 1
            while right - left + 1 - max(all_char.values()) > k:
                all_char[s[left]] -= 1
                left += 1
            max_length = max(max_length,right-left+1)
        return max_length
    
x = Solution()
s = "ABAB"
k = 2
print(x.characterReplacement(s,k))