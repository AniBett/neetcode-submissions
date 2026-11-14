class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen_t = {}
        seen_s = {}
        for i,j in zip(s,t):
            seen_s[i] = 1+seen_s.get(i, 0)
            seen_t[j] = 1+seen_t.get(j, 0)
        if seen_s == seen_t:
            return True
        return False


        