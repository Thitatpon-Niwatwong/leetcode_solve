class Solution:
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = (right - left) * min(height[left],height[right])
            max_area = max(area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


x = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(x.maxArea(height))
