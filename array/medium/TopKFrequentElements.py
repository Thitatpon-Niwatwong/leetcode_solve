class Solution(object):
    def topKFrequent(self, nums, k):
        count = dict()
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for num, length in count.items():
            freq[length].append(num)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


x = Solution()
nums = [1, 1, 1, 2, 2, 3, 3, 3]
k = 2
print(x.topKFrequent(nums, k))
