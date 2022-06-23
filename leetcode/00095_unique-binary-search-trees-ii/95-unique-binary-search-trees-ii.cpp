/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

// A hash function used to hash a tuple
struct hash_tuple {
    template <class T1, class T2>
  
    size_t operator()(const tuple<T1, T2> &x) const {
        return get<0>(x) ^ get<1>(x);
    }
};
 
class Solution {
public: 
    unordered_map<tuple<int, int>, vector<TreeNode*>, hash_tuple> cache;
    vector<TreeNode*> generateTrees(int n) {
        if (n == 0) return vector<TreeNode*>();
        return dfs(1, n);
    }
    
    vector<TreeNode*> dfs(int start, int end) {
        vector<TreeNode*> tree_list;
        if (start > end) {
            tree_list.push_back(NULL);
            return tree_list;
        }
        
        if(cache.count({start, end}) > 0) {
            return cache[{start, end}];
        }
        
        for (int i = start; i <= end; i++) {
            vector<TreeNode*> left = dfs(start, i-1);
            vector<TreeNode*> right = dfs(i + 1, end);
            for (TreeNode *l : left) {
                for (TreeNode *r : right) {
                    TreeNode *root = new TreeNode(i);
                    root->left = l;
                    root->right = r;
                    tree_list.push_back(root);
                }
            }
        }
        
        cache[{start, end}] = tree_list;
        return tree_list;
    }
};
