class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            
            # stack is empty, 
            # but still have ")", "}", or "]" -> not balanced
            if not stack:
                return False
            if c == ')':
                if stack.pop() != '(':
                    return False
            elif c == '}':
                if stack.pop() != '{':
                    return False
            elif c == ']':
                if stack.pop() != '[':
                    return False
        
        return not stack # if stack not empty -> Flase
 