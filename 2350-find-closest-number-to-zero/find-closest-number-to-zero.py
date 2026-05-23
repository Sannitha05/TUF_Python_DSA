class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for x in nums[1:]:
            if abs(x) < abs(ans):
                ans = x
            elif abs(x) == abs(ans) and x > 0:
                ans = x
        return ans