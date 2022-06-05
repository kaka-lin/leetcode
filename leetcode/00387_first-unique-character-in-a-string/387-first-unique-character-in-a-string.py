class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        
        for idx, c in enumerate(s):
            if c not in seen:
                seen[c] = [idx, 1]
            else:
                seen[s[idx]][1] += 1
        
        for k, v in seen.items():
            if v[1] == 1:
                return v[0]
        
        return -1
        