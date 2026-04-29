class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        ans = 0
        max_count = 0
        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(count[s[right]], max_count) # save the max frequency
            # when the window is invalid
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans 