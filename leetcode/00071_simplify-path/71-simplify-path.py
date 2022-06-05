class Solution:
    def simplifyPath(self, path: str) -> str:
        places = [p for p in path.split("/") if p!="." and p!=""]
      
        stack = []
        for p in places:
            if p == "..":
                if len(stack) > 0:
                    stack.pop() # 回上一層的意思
            else:
                stack.append(p)
                
        return "/" + "/".join(stack)
