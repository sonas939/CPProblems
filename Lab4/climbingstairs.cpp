#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <math.h>

using namespace std;

int main(){

    int n = 0;
    int r = 0;
    int k = 0;

    cin >> n;
    cin >> r;
    cin >> k;

    int temp = k + abs(k - r);

    if(abs(n - temp) % 2 == 1)
    {
        temp = max(temp, n + 1);
    }
    else
    {
        temp = max(temp, n);
    }

    temp += r;
    cout << temp << endl;
    return 0;
}