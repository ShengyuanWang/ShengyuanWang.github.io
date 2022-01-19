class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = sum(nums)
        if cnt == 0:
            return 0
        
        cur = 0
        for i in range(cnt):
            cur += (1 - nums[i])
        
        ans = cur
        for i in range(1, n):
            if nums[i - 1] == 0:
                cur -= 1
            if nums[(i + cnt - 1) % n] == 0:
                cur += 1
            ans = min(ans, cur)
        return ans