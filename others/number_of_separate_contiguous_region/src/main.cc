#include <iostream>
#include <string>
#include <queue>
using namespace std;

/* Find separate contiguous regions of "0" */
string BFS(string strArr[], int arrLength) {
  int separate_part = 0;
  queue<pair<int, int>> q;

  // BFS
  int m = arrLength;
  int n = strArr[0].size();
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      if (strArr[i][j] == '0') {
        separate_part += 1;

        q.push({i, j});
        while (!q.empty()) {
          int x = q.front().first;
          int y = q.front().second;
          q.pop();

          strArr[x][y] = '1'; // visited

          if (x+1 < m && strArr[x+1][y] == '0')
            q.push(make_pair(x+1, y));
          if (y+1 < n && strArr[x][y+1] == '0')
            q.push(make_pair(x, y+1));
          if (x-1 >= 0 && strArr[x-1][y] == '0')
            q.push(make_pair(x-1, y));
          if (y-1 >= 0 && strArr[x][y-1] == '0')
            q.push(make_pair(x, y-1));
        }
      }
    }
  }
  strArr[0] = to_string(separate_part);
  return strArr[0];
}

int main() {
  string strArr[] = {"01111", "01101", "00011", "11110"};
  int arrLength = sizeof(strArr) / sizeof(*strArr);
  cout << BFS(strArr, arrLength); // output: 3
  return 0;
}
