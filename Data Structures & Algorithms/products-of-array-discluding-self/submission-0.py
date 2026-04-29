class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums = [1,2,4,6]
        for each index = [1,2,4,6]
        prefix is the product of all numbers on the left side = [1, 1, 2, 8]
        suffix is the product of all numbers on the right side = [48, 24, 6, 1] -> reverse the number
        [6,4,2,1] -> [1,6,24,48] (reverse)
        -> value of the index = prefix[i] * suffix[i]
        """
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        # [1,1,1,1]
        for i in range(n - 2,  -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        res = []
        for i in range(n):
            res.append(prefix[i] * suffix[i])
        return res