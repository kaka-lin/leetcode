class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for curr in tokens:
            if stack and curr in operators:
                b, a = stack.pop(), stack.pop()
                if curr == "+": a += b
                elif curr == "-": a -= b
                elif curr == "*": a *= b
                elif curr == "/": a = int(a / b)
                stack.append(a)
            else:
                stack.append(int(curr))
        
        return stack[0]
