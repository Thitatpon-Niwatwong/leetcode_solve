class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '-':
                a, b = stack.pop(), stack.pop()
                stack.append((b - a))
            elif i == '*':
                stack.append(stack.pop() * stack.pop())
            elif i == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(i))
        return stack[0]


x = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(x.evalRPN(tokens))
