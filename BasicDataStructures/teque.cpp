#include <iostream>
#include <string>
#include <deque>
#include <vector>
#include <sstream>
using namespace std;

int main() {
    long n;
    cin >> n;
    string op;
    vector<string> v;
    deque<unsigned long> front;
    deque<unsigned long> back;
    getline(cin, op);
    for (int i = 0; i < n; i++) {
        getline(cin,op);
        stringstream ss(op);
        while (getline(ss,op,' ')) {
            v.push_back(op);
        }
        if (v[0] == "push_back") {
            if (back.size() < front.size()) {
                back.push_back(stol(v[1]));
            } else {
                back.push_back(stol(v[1]));
                front.push_back(back.front());
                back.pop_front();
            } 
        } else if (v[0] == "push_front") {
            if (front.size() > back.size()) {
                front.push_front(stol(v[1]));
                back.push_front(front.back());
                front.pop_back();
            } else {
                front.push_front(stol(v[1]));
            }
        } else if (v[0] == "push_middle") {
            if (front.size() == back.size()) {
                front.push_back(stol(v[1]));
            }
            else if (front.size() < back.size()) {
                front.push_back(back.front());
                back.pop_front();
                back.push_front(stol(v[1]));
            }
            else {
                back.push_front(stol(v[1]));
            }
        } else {
            unsigned long num = stol(v[1]);
            if (num < front.size()) {
                cout << front[num] << endl;
            }
            else {
                cout << back[num - front.size()] << endl;
            }
        }
        v.clear();
    }
    return 0;
}