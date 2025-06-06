class Solution:
    def dailyTemperatures(self, temperatures):
        result = [0] * len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT ,stackI = stack.pop()
                result[stackI] = i - stackI
            stack.append([t,i])
        return result

x = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(x.dailyTemperatures(temperatures))
