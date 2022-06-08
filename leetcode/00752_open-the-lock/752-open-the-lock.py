# [Not accepted] Time Limit Exceeded
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"
        step = 0
        queue = [(start, step)]
        visited = set(start)
        directions = [1, -1]
        
        while queue:
            cur_num, step = queue.pop(0)
            if cur_num == target:
                return step
            elif cur_num in deadends:
                continue
            
            for i in range(len(cur_num)):
                for d in directions:
                    # Time Limit Exceeded:
                    # rotate_num = int(cur_num[i]) + d
                    # rotate_num = 9 if rotate_num == -1 else rotate_num
                    # new_num = cur_num[:i] + str(rotate_num) + cur_num[i+1:]
                    moved = (int(cur_num[i]) + d) % 10 # -1 % 10 = 9
                    new_num = cur_num[:i] + str(moved) + cur_num[i+1:]
                    if new_num not in visited:
                        queue.append((new_num, step+1))
                        visited.add(new_num)
        
        return -1
