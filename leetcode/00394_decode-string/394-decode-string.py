class Solution:
    def decodeString(self, s: str) -> str:
        repeated = [[]]
        encoded_string = []
        ans = ""
        
        for c in s:
            if c == "[":
                encoded_string.append([])
                repeated.append([])
                continue
            if c == "]":
                k = int("".join(repeated[-2]))
                string = "".join(encoded_string[-1])
                ans = k * string
                
                repeated.pop(-2)
                encoded_string.pop()
                
                if len(encoded_string) < 1:
                    encoded_string.append([])             
                encoded_string[-1].append(ans) 
                continue
                
            if ord(c) <= 57:
                repeated[-1].append(c)
            else:
                if len(encoded_string) < 1:
                    encoded_string.append([]) 
                encoded_string[-1].append(c)
            
        
        return "".join(encoded_string[-1])
        
        
