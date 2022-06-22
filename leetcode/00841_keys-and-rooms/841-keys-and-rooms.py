class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
            queue = [rooms[0]]
            visited = {0}
            
            while queue:
                keys = queue.pop(0)
                for key in keys:
                    if key < 0 or key >= len(rooms):
                        continue
                    
                    if key not in visited:
                        queue.append(rooms[key])
                        visited.add(key)
                        if len(visited) == len(rooms):
                            return True
            
            return len(visited) == len(rooms)

