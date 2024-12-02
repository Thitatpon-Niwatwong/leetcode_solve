class Solution:
    def isValid(self, s):
        all_bracket = []
        bracket = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        for i in s:
            if i in bracket:
                if all_bracket:
                    if bracket[i] == all_bracket[-1] and all_bracket:
                        all_bracket.pop()
                    else:
                        return False
                else:
                    return False
            elif i in bracket.values():
                all_bracket.append(i)
        return not all_bracket

x = Solution()
s = "()[]{}"
print(x.isValid(s))