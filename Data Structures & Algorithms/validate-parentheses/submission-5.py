class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        matching = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            # Push opening brackets onto the stack
            if char not in matching:
                stack.append(char)
            # For closing brackets:
            else:
                if len(stack) == 0:
                    return False
                elif matching[char] == stack[len(stack) -1]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
        # 1. Check whether the stack is empty
        # 2. Pop the most recent opening bracket
        # 3. Check whether it matches

    # Return True only if the stack is empty

        