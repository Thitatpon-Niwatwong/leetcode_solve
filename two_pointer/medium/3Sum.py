class Solution(object):
    def threeSum(self, nums):
        result = []
        sorted_nums = sorted(nums)
        for i,v in enumerate(sorted_nums):
            if i > 0 and v == sorted_nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                sum = v + sorted_nums[left] + sorted_nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([v,sorted_nums[left],sorted_nums[right]])
                    left += 1
                    while sorted_nums[left] == sorted_nums[left-1] and left < right:
                        left += 1
        return result


x = Solution()
nums = [-1,0,1,2,-1,-4]
print(x.threeSum(nums))