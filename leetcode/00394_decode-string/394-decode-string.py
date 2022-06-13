# [By kaka]
# class Solution:
#     def decodeString(self, s: str) -> str:
#         repeated = [[]]
#         encoded_string = []
#         ans = ""
        
#         for c in s:
#             if c == "[":
#                 encoded_string.append([])
#                 repeated.append([])
#                 continue
#             if c == "]":
#                 k = int("".join(repeated[-2]))
#                 string = "".join(encoded_string[-1])
#                 ans = k * string
                
#                 repeated.pop(-2)
#                 encoded_string.pop()
                
#                 if len(encoded_string) < 1:
#                     encoded_string.append([])             
#                 encoded_string[-1].append(ans) 
#                 continue
                
#             if ord(c) <= 57:
#                 repeated[-1].append(c)
#             else:
#                 if len(encoded_string) < 1:
#                     encoded_string.append([]) 
#                 encoded_string[-1].append(c)
                    
#         return "".join(encoded_string[-1])

 
class Solution:
    def decodeString(self, s: str) -> str:   
        stack = []
        curNum = 0
        curString = ''
        
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num * curString
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            else:
                curString += c
                
        return curString