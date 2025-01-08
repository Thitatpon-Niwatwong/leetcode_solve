class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = 0
        res = []
        for i in candies:
            if i > max_candies:
                max_candies = i
        for n in candies:
            if n + extraCandies >= max_candies:
                res.append(True)
            else:
                res.append(False)
        return res
