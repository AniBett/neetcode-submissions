class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        max_len = 0
        for right in range(0, len(s)):
        
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            current_len = len(seen)
            max_len = max(current_len, max_len)
        return max_len

