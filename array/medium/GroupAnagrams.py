class Solution(object):
    def groupAnagrams(self, strs):
        groupAnagram = dict()
        for word in strs:
            anagram = [0] * 26
            for char in word:
                anagram[ord(char) - ord('a')] += 1
            tuple_anagram = tuple(anagram)
            if tuple_anagram in groupAnagram:
                groupAnagram[tuple_anagram].append(word)
            else:
                groupAnagram[tuple_anagram] = [word]
        return list(groupAnagram.values())


x = Solution()
strs = ["act","pots","tops","cat","stop","hat"]
print(x.groupAnagrams(strs))


                