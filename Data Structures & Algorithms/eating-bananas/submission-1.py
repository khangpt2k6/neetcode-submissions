from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # koko eating bananas
        """
        what is the k value so that koko can finish those banana in h time 
        each time koko can only each 1 pile 
        naive approach
        
        """
        def can_finish(k):
            total = 0
            for pile in piles:
                total += ceil(pile / k)
            return total <= h
        
        # the minimum k is 1, the maxium k could be max(piles)
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if can_finish(mid): # total <=  h
                # if satisfy the condition
                right = mid # try the smaller k, okay this k is valid, how about we continue to try with smaller k
            else:
                left = mid + 1 # try the bigger k 
        return left 