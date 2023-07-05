//using variation of bellman ford algorithm from book
#include <iostream>
#include <vector>
#define INF 1e9

using namespace std;

struct node {
    bool hauntedHole;
    long long dist;
    bool graveStones;
    int x2;
    int y2;
    int time;
};

bool isValid(int r,int c,int w,int h) {
    if (r < 0 || c < 0) {
        return false;
    }
    
    if (r >= w || c >= h) {
        return false;
    }

    return true;
}

int main() {
    while (true) {
        int w,h;
        cin >> w >> h;
        if (w == 0 && h == 0) {
            break;
        }
        node grid[w][h];
        for (int i = 0; i < w; i++) {
            for (int j = 0; j < h; j++) {
                grid[i][j].hauntedHole = false;
                grid[i][j].dist = INF;
                grid[i][j].graveStones = false;
            }
        }
        int g;
        cin >> g;
        for (int i = 0; i < g; i++) {
            int x,y;
            cin >> x >> y;
            grid[x][y].graveStones = true;
        }
        int e;
        cin >> e;
        for (int i = 0; i < e; i++) {
            int x,y,x1,y1,t;
            cin >> x >> y >> x1 >> y1 >> t;
            grid[x][y].hauntedHole = true;
            grid[x][y].x2 = x1;
            grid[x][y].y2 = y1;
            grid[x][y].time = t;
        }

        grid[0][0].dist = 0;
        for (int i = 0; i < w*h - 1; i++) {
            for (int r = 0; r< w; r++) {
                for (int c = 0; c < h; c++) {
                    if (r==w-1 && c == h-1) {
                        continue;
                    }
                    if (grid[r][c].dist != INF && !grid[r][c].graveStones) {
                        if (grid[r][c].hauntedHole) {
                            if (grid[grid[r][c].x2][grid[r][c].y2].dist > grid[r][c].dist + grid[r][c].time) {
                                grid[grid[r][c].x2][grid[r][c].y2].dist = grid[r][c].dist + grid[r][c].time;
                            }
                        }
                        else {
                            if (isValid(r-1,c,w,h)) {
                                if (grid[r][c].dist+1 < grid[r-1][c].dist && !grid[r-1][c].graveStones) {
                                    grid[r-1][c].dist = grid[r][c].dist + 1;
                                }
                            }
                            if (isValid(r,c-1,w,h)) {
                                if (grid[r][c].dist+1 < grid[r][c-1].dist && !grid[r][c-1].graveStones) {
                                    grid[r][c-1].dist = grid[r][c].dist + 1;
                                }
                            }
                            if (isValid(r+1,c,w,h)) {
                                if (grid[r][c].dist+1 < grid[r+1][c].dist && !grid[r+1][c].graveStones) {
                                    grid[r+1][c].dist = grid[r][c].dist + 1;
                                } 
                            }
                            if (isValid(r,c+1,w,h)) {
                                if (grid[r][c].dist+1 < grid[r][c+1].dist && !grid[r][c+1].graveStones) {
                                    grid[r][c+1].dist = grid[r][c].dist + 1;
                                }
                            }
                        }
                    }
                }
            }
        }
        bool negCycle = false;
        for (int r = 0; r < w; r++) {
            for (int c = 0; c < h; c++) {
                if (r==w-1 && c == h-1) {
                        continue;
                }
                if (grid[r][c].dist != INF && !grid[r][c].graveStones) {
                    if (grid[r][c].hauntedHole) {
                        if (grid[grid[r][c].x2][grid[r][c].y2].dist > grid[r][c].dist + grid[r][c].time) {
                            negCycle = true;
                            break;
                        }
                    }
                    else {
                        if (isValid(r-1,c,w,h)) {
                            if (grid[r-1][c].graveStones) {
                                continue;
                            }
                            if (grid[r-1][c].dist > grid[r][c].dist + 1) {
                                negCycle = true;
                                break;
                            }
                        }
                        if (isValid(r,c-1,w,h)) {
                            if (grid[r][c-1].graveStones) {
                                continue;
                            }
                            if (grid[r][c-1].dist > grid[r][c].dist + 1) {
                                negCycle = true;
                                break;
                            }
                        }
                        if (isValid(r+1,c,w,h)) {
                            if (grid[r+1][c].graveStones) {
                                continue;
                            }
                            if (grid[r+1][c].dist > grid[r][c].dist + 1) {
                                negCycle = true;
                                break;
                            }
                        }
                        if (isValid(r,c+1,w,h)) {
                            if (grid[r][c+1].graveStones) {
                                continue;
                            }
                            if (grid[r][c+1].dist > grid[r][c].dist + 1) {
                                negCycle = true;
                                break;
                            }
                        }
                    }
                }
            }
        }

        if (negCycle) {
            cout <<"Never" << endl;
        } 
        else if (grid[w-1][h-1].dist == INF) {
            cout << "Impossible" << endl;
        }
        else {
            cout << grid[w-1][h-1].dist << endl;
        }
    }
}
