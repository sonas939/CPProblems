#include <iostream>
#include <string>
#include <math.h>
using namespace std;

int main() {

    while (true) {
        long long n;
        cin >> n;
        if (n == 4) {
            break;
        }

        long long count = 1;
        while (true) {
            long long sum = 0;
            long long num = n;
            for (int i = 2; i <= ceil(sqrt(n)) && n != 1; i++) {
                while (n%i == 0) {
                    n /= i;
                    sum += i;
                }
            }
            if (n != 1) {
                sum += n;
            }

            if (sum == num) {
                cout << num << " " << count << endl;
                break;
            }
            else {
                n = sum;
            }
            count += 1;
        }
    }
    return 0;
}