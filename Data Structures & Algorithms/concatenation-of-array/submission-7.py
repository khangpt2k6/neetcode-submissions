class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        k = len(nums)
        ans = [0] * (2 * k)
        for i in range(len(nums)):
            ans[i] = nums[i]
        for i in range(len(nums)):
            ans[k] = nums[i]
            k += 1
        return ans
        