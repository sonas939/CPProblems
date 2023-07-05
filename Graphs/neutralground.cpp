#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

const int MAX_NUM = 1e6;

int main() {
    int w, h;
    cin >> w >> h;
    vector<vector<int> > grid(h, vector<int> (w, -1));
    for (int i = 0; i < h; i++) {
        string usr;
        cin >> usr;
        for (int j = 0; j < w; j++) {
            if (usr[j] == 'A') {
                continue;
            }
            else if (usr[j] == 'B') {
                grid[i][j] = -2;
            }
            else {
                grid[i][j] = static_cast<int>(usr[j]) - static_cast<int>('0');
            }
        }
    }

    int x[] = {-1,0,1,0};
    int y[] = {0,-1,0,1};
    vector<vector<pair<int,int>> > adj_list;
    adj_list.assign(w*h*2+2, vector<pair<int,int>>());

    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if (grid[i][j] >= 0) {
                adj_list[i*w+1+j].emplace_back(i*w+1+j+w*h,grid[i][j]);
                adj_list[i*w+1+j+w*h].emplace_back(i*w+1+j,0);
            }
            else {
                adj_list[i*w+1+j].emplace_back(i*w+1+j+w*h,MAX_NUM);
                adj_list[i*w+1+j+w*h].emplace_back(i*w+1+j,0);
            }

            if (grid[i][j] == -1) {
                adj_list[0].emplace_back(i*w+1+j,MAX_NUM);
                adj_list[i*w+1+j].emplace_back(0,0);
            }
            else if (grid[i][j] == -2) {
                adj_list[i*w+1+j+w*h].emplace_back(w*h*2+1,MAX_NUM);
                adj_list[w*h*2+1].emplace_back(i*w+1+j+w*h,0);
            }
            for (int k = 0; k < 4; k++) {
                if (i+x[k] >= 0 && j+y[k] >= 0 && i+x[k] < h && j+y[k] < w){
                    adj_list[i*w+1+j+w*h].emplace_back((i+x[k]) * w + 1 + j + y[k],MAX_NUM);
                    adj_list[(i+x[k]) * w + 1 + j + y[k]].emplace_back(i*w+1+j+w*h,0);
                }
            }
        }
    }

    long long total = 0;
    vector<int> parent(w*h*2+2,-1);
    vector<int> visited(w*h*2+2,-1);

    bool bfs = false;
    while (true) {
        queue<int> q;
        q.push(0);
        visited[0] = MAX_NUM;
        parent[0] = -1;
        int minFlow = 0;
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            for (int i = 0; i < adj_list[node].size(); i++) {
                int edge = adj_list[node][i].first;
                int weight = adj_list[node][i].second;
                if (visited[edge] == -1 && weight > 0) {
                    q.push(edge);
                    parent[edge] = node;
                    visited[edge] = visited[node];
                    if (weight < visited[node]) {
                        visited[edge] = weight;
                    }
                    if (edge == w*h*2+1) {
                        bfs = true;
                    }
                }
            }
        }
        if (!bfs) {
            break;
        }

        int sink = w*h*2+1;
        long long maxFlow = visited[w*h*2+1];
        while (sink != 0) {
            int u = parent[sink];
            for (int i = 0; i < adj_list[sink].size(); i++) {
                if (adj_list[sink][i].first == u) {
                    adj_list[sink][i].second += maxFlow;
                }
            }
            for (int j = 0; j < adj_list[u].size();j++) {
                if (adj_list[u][j].first == sink) {
                    adj_list[u][j].second -= maxFlow;
                }
            }
            sink = u;
        }
        total += maxFlow;
        visited.assign(w*h*2+2,-1);
        bfs = false;
    }

    cout << total << endl;
}