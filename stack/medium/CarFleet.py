class Solution(object):
    def carFleet(self, target, position, speed):
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            time = (target-p) /s
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        return len(stack)


x = Solution()
target = 10
position = [6,8]
speed = [3,2]
print(x.carFleet(target, position, speed))
