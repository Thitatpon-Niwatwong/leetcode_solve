class Solution:
    def generateParenthesis(self, n):
        stack = []
        result = []
        def backtrack(openN,closeN):
            if openN == closeN == n:
                result.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN+1,closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtrack(openN,closeN+1)
                stack.pop()
        backtrack(0,0)
        return result
    
x = Solution()
n = 2
print(x.generateParenthesis(n))