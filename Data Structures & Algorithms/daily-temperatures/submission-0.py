class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            # While the current temperature is warmer
            while stack and temp > temperatures[stack[-1]]:
                test = stack.pop()
                result[test] = i-test
            stack.append(i)
          


        return result
        
        