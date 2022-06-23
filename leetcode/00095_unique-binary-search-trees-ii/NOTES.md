# Solution

```
start     ~           end
1, 2, 3, ..., k, ..., n


假設 root 為 k，那麼

- 左子樹: 1 ~ K-1, left = dfs(start, idx - 1)
- 右子樹: k+1 ~ n, right = dfs(idx + 1, end)

如下:

           k
         /   \
(1 ~ k-1)     (k+1 ~ n)

依此類推。
```

* 遞迴終止條件: `當 start > end 時，return null`

    Example:

    ```
    假設 n = 1 => start = 1, end = 1 => (1, 1)

                1
              /   \
        (1, 0)     (2, 1)

    => 當 start > end 時，retun [None]
  ```

## Reference

- [[Leetcode 95] Unique Binary Search Tree II](https://www.youtube.com/watch?v=GZ0qvkTAjmw)
- [Unique Binary Search Trees II](https://www.youtube.com/watch?v=hQn61BjdA7M)
