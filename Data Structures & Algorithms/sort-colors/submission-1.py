class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # mid keep track of 1
        # left is 0 and right is 2
        left = 0
        right = len(nums) - 1
        mid = 0
        while mid <= right:
            # if 0, swap with left
            if nums[mid] == 0:
                nums[mid], nums[left] = nums[left], nums[mid]
                mid += 1
                left += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
        return nums
        