class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_sum = 0
        for num in nums:

            if current_sum < 0:
                current_sum = 0
            
            current_sum += num

            current_max = max(current_max, current_sum)
        return current_max