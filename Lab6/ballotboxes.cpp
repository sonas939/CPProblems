#include <iostream>
#include <string>
#include <queue>
#include <tuple>
#include <cmath>

using namespace std;

int main() {
    priority_queue<tuple<double,long long,long long> > pq;
    long long nCities, nBoxes;
    cin >> nCities >> nBoxes;
    while (nCities != -1 && nBoxes != -1) {
        for (long long i = 0; i < nCities; i++) {
            long long in;
            cin >> in;
            tuple<double, long long, long long> tuple2(in,in,1);
            pq.push(tuple2);
        }
        nBoxes -= nCities;
        while (nBoxes > 0) {
            tuple<double, long long, long long> tuple3 = pq.top();
            long long max = get<1>(tuple3);
            long long n = get<2>(tuple3);
            pq.pop();
            tuple<double, long long, long long> tuple1((double)max/(n+1),max,n+1);
            pq.push(tuple1);
            nBoxes -= 1;
        }
        tuple<double, long long, long long> tuple4 = pq.top();
        cout << ceil(get<0>(tuple4)) << endl;
        cin >> nCities >> nBoxes;
        pq = priority_queue<tuple<double,long long,long long> > ();
    }
}
