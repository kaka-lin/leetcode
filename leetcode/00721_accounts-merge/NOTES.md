# Solution

Ref: [Python Simple DFS with explanation!!!](https://leetcode.com/problems/accounts-merge/discuss/109161/Python-Simple-DFS-with-explanation!!!)

## Explation

Accounts
```python
[
  ["John", "johnsmith@mail.com", "john00@mail.com"], # Account 0
  ["John", "johnnybravo@mail.com"], # Account 1
  ["John", "johnsmith@mail.com", "john_newyork@mail.com"],  # Account 2
  ["Mary", "mary@mail.com"] # Account 3
]
```

Next, build an `emails_accounts_map` that maps an email to a list of accounts, which can be used to track which email is linked to which account. This is essentially our graph.

```python
# emails_accounts_map of email to account ID
{
  "johnsmith@mail.com": [0, 2],
  "john00@mail.com": [0],
  "johnnybravo@mail.com": [1],
  "john_newyork@mail.com": [2],
  "mary@mail.com": [3]
}
```
