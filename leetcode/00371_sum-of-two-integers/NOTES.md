# Solution

## Solution 1: Bit manipulation

Ref: https://www.youtube.com/watch?v=qq64FrA2UXQ

### The example of Bit manipulation

```
2 = "10"
3 = "11"

123 + 39:

 1111111
  1111011 (123)
+  100111 (39)
 --------
 10100010 (162)

Step 1:
  1 + 1 = 2, 2 = "10"
  所以放 0, carry = 1

Step 2:
  1 + 1 + 1 = 3, 3 = "11"
  所以放 1, carry = 1

Step 2:
  1 + 0 + 1 = 2, 2 = "10"
  所以放 0, carry = 1

依此類推，可得答案
```

### Tips: AND, XOR, Left shift

```
if we use "AND(&)":
   111 -> this is called carry
    111
    111
    ---
    111 -> we can find carry

=> carry need to left shift "<<"

if we use "xor(^)":
   1
    1010
    1100
    -----
    0110 -> "simulating addition"

    1 + 1 = 2, 2 = "10"

left shit:
   111 -> AND (&)
    111
    111
    ---
    000 > XOR (^)

then, the carry apply left shit
```

### Conclusion

- Step 1: Find carries (&)
- Step 2: Do the addition (^)
- Step 3: "b" holds left-shifted carry
- Step 4: repeat Step 1 - 3

```python
while b:
    carry = a & b
    a ^= b
    b = carry << 1
return a
```
