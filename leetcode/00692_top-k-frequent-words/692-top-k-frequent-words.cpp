typedef pair<string, int> Node;
class Compare {
 public:
  bool operator()(const Node& a, const Node& b) const {
    if (a.second == b.second) {
        // less
        return (a.first > b.first);
    }
    // greater
    return a.second < b.second;
  }
};

class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        // count
        unordered_map<string, int> count;
        for (const auto& word : words)
            ++count[word];
        
        // priority queue by frequency
        priority_queue<Node, vector<Node>, Compare> q;
        for (const auto& kv: count) {
            q.push(kv);
        }
        
        vector<string> ans;
        while (!q.empty()) {
            ans.push_back(q.top().first);
            q.pop();
            
            if (ans.size() >= k) 
                break;
        }
        
        return ans;
    }
};