class Solution(object):
    def containsDuplicate(self, nums):
        setNums = set()
        for i in nums:
            if i in setNums:
                return True
            setNums.add(i)
        return False
