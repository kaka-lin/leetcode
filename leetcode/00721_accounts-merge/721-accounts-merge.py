class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails_accounts_map = {}
        visited_accounts = set()
        ans = []
        
        # Build up the graph.
        # Example:
        # [["John", "johnsmith@mail.com", "john00@mail.com"], # Account 0
        # ["John", "johnnybravo@mail.com"], # Account 1
        # ["John", "johnsmith@mail.com", "john_newyork@mail.com"],  # Account 2
        # ["Mary", "mary@mail.com"]] # Account 3
        # emails_accounts_map of email to account ID
        # {
        #   "johnsmith@mail.com": [0, 2],
        #   "john00@mail.com": [0],
        #   "johnnybravo@mail.com": [1],
        #   "john_newyork@mail.com": [2],
        #   "mary@mail.com": [3]
        # }
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                if email in emails_accounts_map:
                    emails_accounts_map[email].append(i)
                else:
                    emails_accounts_map[email] = [i]
            
        # DFS for traversing accounts.
        def dfs(i, emails):
            if i in visited_accounts:
                return
            
            visited_accounts.add(i)
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neighbor in emails_accounts_map[email]:
                    dfs(neighbor, emails)
        
        # Perform DFS for accounts and add to results.
        for i, account in enumerate(accounts):
            if i in visited_accounts:
                continue
            name, emails = account[0], set()
            dfs(i, emails)
            ans.append([name] + sorted(emails))
        
        return ans
      