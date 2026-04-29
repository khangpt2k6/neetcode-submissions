class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        left = 0
        ans = 0
        for right in range(len(s)):
            count[s[right]] += 1 # this is the length of the string
            while count[s[right]] > 1: # if this is invalid
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1) # after all it is valid
        return ans 
        
                