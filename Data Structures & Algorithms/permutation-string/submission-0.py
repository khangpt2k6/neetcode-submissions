class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        permutation or anagram is just the frequency of the character of two string 
        """
        c1 = defaultdict(int)
        c2 = defaultdict(int)
        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2:
            return False
        for i in range(l1):
            c1[s1[i]] += 1
            c2[s2[i]] += 1
        # checking the first window
        if c1 == c2:
            return True 
        
        # sliding window 
        for i in range(l1, l2):
            c2[s2[i - l1]] -= 1
            if c2[s2[i - l1]] == 0:
                del c2[s2[i - l1]]
            c2[s2[i]] += 1
            if c1 == c2:
                return True 
        return False

                