class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        left = 0
        target_counts ={}
        window_counts = {}
        for i,char in enumerate(s1):
            target_counts[char] = target_counts.get(char, 0) + 1
            window_counts[s2[i]] = window_counts.get(s2[i],0) + 1
        for right in range(len(s1), len(s2)):
            if target_counts == window_counts:
                return True
        
            window_counts[s2[right]]=window_counts.get(s2[right],0)+1
            window_counts[s2[left]] = window_counts.get(s2[left],0) - 1
            if window_counts[s2[left]] <= 0:
                del window_counts[s2[left]]
            left += 1
        if target_counts == window_counts:
                return True 
        return False




        