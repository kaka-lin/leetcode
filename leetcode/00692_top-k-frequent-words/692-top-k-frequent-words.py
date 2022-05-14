class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {} # count_dict
        for c in words:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        
        # sorted: frequency
        #sorted_list = [k for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)]
        sorted_list = [k for k, v in sorted(d.items(), key=cmp_to_key(self.compare))]

        # Top K
        return sorted_list[:k]
    
    def compare(self, x, y):
        # x: post, y: prev
        # It needs to return -1, 0, or 1
        if x[1] == y[1]:
            # lexicographical order: greater
            return 1 if x[0] > y[0] else -1
        else:
            # less
            return 1 if x[1] < y[1] else -1
        