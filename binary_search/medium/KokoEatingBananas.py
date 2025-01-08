import math

class Solution:
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)

        while left <= right:
            medium = (left + right)//2
            count = 0

            for pile in piles:
                count += math.ceil(pile/medium)
            if count <= h:
                right = medium - 1
            else:
                left = medium + 1
        return left


x = Solution()
piles = [1, 4, 3, 2]
h = 9
print(x.minEatingSpeed(piles, h))
