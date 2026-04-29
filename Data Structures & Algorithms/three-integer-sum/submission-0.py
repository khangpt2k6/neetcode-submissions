class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums[left] + nums[right] == -nums[i]
        n = len(nums)
        res = []
        nums.sort()
        # we havce to skip the duplicate also 
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue # skip the duplicate
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if total == 0:
                    res.append([nums[left], nums[right], nums[i]])
                    # skip all the duplciate 
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1 # don't touch that value anymore
                elif total < 0:
                    left += 1
                else: 
                    right -= 1
        return res
    