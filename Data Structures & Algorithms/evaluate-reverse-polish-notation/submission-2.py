class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ("+", "-", "*", "/")
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                right = int(stack.pop())
                left = int(stack.pop())
                if token == "+":
                    result = left + right
                elif  token == "-":
                    result = left - right
                elif token == "*":
                    result = left * right
                else:
                    result = left/right

                stack.append(int(result))
        return stack[-1]


        