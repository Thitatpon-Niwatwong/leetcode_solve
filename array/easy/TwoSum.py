class Solution(object):
    def twoSum(self, nums, target):
        dictNums = dict()
        for i,v in enumerate(nums):
            if target - v in dictNums:
                return dictNums[target - v], i
            dictNums[v] = i

x = Solution()
nums = [2,7,11,15] 
target = 9
print(x.twoSum(nums,target))