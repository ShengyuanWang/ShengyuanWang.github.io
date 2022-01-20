class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            m1 = m2 = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] > m2:
                    m2 = nums[j]
                if nums[j] < m1:
                    m1 = nums[j]
                res += (m2 - m1)
        return res
