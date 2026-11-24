class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        seen = {}
        max_len = 0
        for  right in range(len(fruits)):
            seen[fruits[right]] = seen.get(fruits[right],0) + 1
            while len(seen) > 2:
                seen[fruits[left]] = seen.get(fruits[left],0) - 1
                if seen[fruits[left]] <= 0:
                    del seen[fruits[left]]
                left += 1
            max_len = max(right-left+1, max_len)
        return(max_len)

            
        