class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        array have sort in ascending order
        nums = [1,2,3,4,5,6]
        -> rotate k -> [3,4,5,6,1,2]
        -> the minimum value of the array 
        when consider it have two area:
        [3,4,5,6] & [1,2]
        we should do the binary search on this area
        [4,5,0,1,2,3]
        mid = (left + right) // 2

        the mid > the right value: 
            move the left to the right # the minimum is on the right
        else:
            move the right to left # because the minimum is on the left
        """
        left, right = 0, len(nums) - 1
        ans = float('inf')
        while left < right:
            mid = (left + right) // 2
            ans = min(ans, nums[mid])
            if nums[mid] > nums[right]:
                left = mid + 1 # the smaller is on the right
            else: 
                right = mid # the smaller is on the left        
        return nums[left]