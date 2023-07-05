#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
    int testCases;
    cin >> testCases;

    for (int caseNum = 1; caseNum <= testCases; caseNum++) {
        int n, p, q;
        cin >> n >> p >> q;

        vector<int> a(p+1), b(q+1), c;
        unordered_map<int, int> indexes;

        for (int i = 0; i < p+1; i++) {
            cin >> a[i];
            indexes[a[i]] = i;
        }

        for (int i = 0; i < q+1; i++) {
            cin >> b[i];
            if (indexes.find(b[i]) != indexes.end()) {
                c.push_back(indexes[b[i]]);
            }
        }

        vector<int> l;
        for (int i = 0; i < c.size(); i++) {
            if (l.empty() || l.back() < c[i]) {
                l.push_back(c[i]);
            } else {
                int low = 0, high = l.size() - 1, mid=(low + high) / 2;
                while (low <= high) {
                    mid = (low + high) / 2;
                    if (l[mid] < c[i]) {
                        low = mid + 1;
                    } else {
                        high = mid - 1;
                    }
                }
                l[low] = c[i];
            }
        }

        cout << "Case " << caseNum << ": " << l.size() << endl;
    }

    return 0;
}