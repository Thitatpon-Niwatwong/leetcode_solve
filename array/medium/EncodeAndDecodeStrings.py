class Solution:
    def encode(self, strs):
        new_word = ""
        for word in strs:
            length = len(word)
            new_word += str(length) + '#' + word
        return new_word

    def decode(self, strs):
        original_word = []
        i = 0
        while i < len(strs):
            j = i
            while strs[j] != '#':
                j += 1
            length = int(strs[i:j])
            original_word.append(strs[j+1:j+length+1])
            i = j+length+1
        return original_word


x = Solution()
strs = ["we", "say", ":", "yes", "!@#$%^&*()"]
print(x.encode(strs))
y = x.encode(strs)
print(x.decode(y))
