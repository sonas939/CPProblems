#include <iostream>
#include <string>
#include <math.h>
using namespace std;

int main() {
    string s;
    cin >> s;

    long long sLength = s.size();
    if (sLength >= 8) { //length unique after 11!
        double sum = 1;
        long long i = 1;
        while (floor(sum) != sLength) {
            sum += log10(i);
            i += 1;
        }
        cout << i-1 << endl;
    }
    else { //if length means num less than 10!
        long long num = stoi(s);
        long long sum = 1;
        for (int i = 1; i <= num;i++) {
            sum *= i;
            if (sum == num) {
                cout << i << endl;
                break;
            }
        }
    }
    return 0;
}