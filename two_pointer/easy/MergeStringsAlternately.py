class Solution(object):
    def mergeAlternately(self, word1, word2):
        a = len(word1)
        b = len(word2)
        c = 0
        d = 0
        new_word = ""
        while a != 0 or b != 0:
            if a > 0:
                new_word += word1[c]
                c += 1
                a -= 1
            if b > 0:
                new_word += word2[d]
                d += 1
                b -= 1
        return new_word

x = Solution()
word1 = "ab"
word2 = "pqrs"
print(x.mergeAlternately(word1,word2))

            

            