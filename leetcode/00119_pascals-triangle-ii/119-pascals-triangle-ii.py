# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         pascal_list = [1]
#        
#         for row in range(1, rowIndex + 1):
#             # previous row
#             prev_pascal_list = pascal_list
#           
#             pascal_list = []
#             # new row: numCol =  len(prev_pascal_list) + 1
#             for col in range(len(prev_pascal_list) + 1):
#                 if col == 0 or col == len(prev_pascal_list):
#                     pascal_list.append(1)
#                 else:
#                     pascal_list.append(prev_pascal_list[col-1] + prev_pascal_list[col])
#       
#         return pascal_list


# recursive
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal_list = self.helper(rowIndex, [1])
        return pascal_list
    
    def helper(self, rowIndex, pascal_list):
        if ((rowIndex + 1) == len(pascal_list)):
            return pascal_list
        
        prev_pascal_list = pascal_list
        pascal_list = []
        for col in range(len(prev_pascal_list) + 1):
            if col == 0 or col == len(prev_pascal_list):
                pascal_list.append(1)
            else:
                pascal_list.append(prev_pascal_list[col-1] + prev_pascal_list[col])
        
        ans = self.helper(rowIndex, pascal_list)
        return ans