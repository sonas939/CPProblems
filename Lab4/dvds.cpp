#include <iostream>
#include <vector>

using namespace std;

int main() {

    int num = 0;
    cin >> num;

    for(int i = 0; i < num; i++) 
    {
        int val = 0;
        cin >> val;
        vector<int> dvds;

        for(int j = 0; j < val; j++) 
        {
            int elem;
            cin >> elem;
            dvds.push_back(elem);
        }
        int target = 0;
        for(int k = 0; k < val; k++) 
        {
            if(dvds[k] == target + 1) 
            {
                target++;
            }
        }
        cout << val - target << endl;
    }
}