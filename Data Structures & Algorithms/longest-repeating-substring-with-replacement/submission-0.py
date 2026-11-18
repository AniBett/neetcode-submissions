class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counts = {}
        max_len = 0
        max_freq = 0

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            max_freq = max(counts[s[right]], max_freq)
         

        
            while (right-left+1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1

  
            max_len = max(right-left+1, max_len)

        return max_len

        