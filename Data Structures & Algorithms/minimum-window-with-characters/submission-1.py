class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_counts = {}
        window_counts = {}
        left = 0
        formed = 0
        min_len = float('inf')
        result = ""

        # Build target_counts from t
        for char in t:
            target_counts[char] = target_counts.get(char, 0) + 1
        for right in range(len(s)):
            # Add s[right] to window_counts
            window_counts[s[right]] = window_counts.get(s[right], 0) + 1
            if window_counts[s[right]] == target_counts.get(s[right]):
                formed += 1

            # Increase formed if a requirement is newly satisfied

            while formed == len(target_counts):
                # Update the shortest valid substring
                if min_len > right-left+1:
                    result = s[left:right+1]
                    min_len = right-left+1
                window_counts[s[left]] = window_counts.get(s[left], 0) -1

                if s[left] in target_counts:
                    if window_counts[s[left]] < target_counts[s[left]]:
                        formed -= 1
                if window_counts[s[left]] <= 0:
                    del window_counts[s[left]]
                left += 1
                # Remove s[left] from the window
                # Decrease formed if a requirement becomes unsatisfied

                # Move left forward

        return result

        
        