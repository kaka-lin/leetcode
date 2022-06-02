# Solution

## Solution 1: Rotate Groups of Four Cells

Example:

```
n = 3, 3x3 Matrix

 1  '2'  3　　　 　　  7  '4'  1　

'4'  5  '6'   -->   '8'  5  '2'　　

 7  '8'  9 　　　 　　 9  '6'  3


i: range(n // 2 + n % 2), (0,1)
j: range(n // 2)        , (0)

n = 3, i = 0, j = 0:
temp = (2, 0), 7 | temp = [n - 1 - j][i]
(2, 0) = (2, 2)  | [n - 1 - j][i] = [n - 1 - i][n - j - 1]
(2, 2) = (0, 2)  | [n - 1 - i][n - j - 1] = [j][n - 1 - i]
(0, 2) = (0, 0)  | [j][n - 1 - i] = [i][j]
(0, 0) = temp    | [i][j] = temp

n = 3, i = 1, j = 0:
temp = (2, 1), 8 | temp = [n - 1 - j][i]
(2, 1) = (1, 2)  | [n - 1 - j][i] = [n - 1 - i][n - j - 1]
(1, 2) = (0, 1)  | [n - 1 - i][n - j - 1] = [j][n - 1 - i]
(0, 1) = (1, 0)  | [j][n - 1 - i] = [i][j]
(1, 0) = temp    | [i][j] = temp
```
