#include <iostream>
#include <vector>
#include <string>

using namespace std;

int rankLevel(int x) {
    if (x >= 21) 
    {
        return 2;
    } 
    else if (x >= 16) 
    {
        return 3;
    } 
    else if (x >= 11) 
    {
        return 4;
    } 
    else 
    {
        return 5;
    }
}

int main() {
    string status = "";
    cin >> status;

    int rank = 25;
    int stars = 0;
    int consecutive = 0;

    for (int i = 0; i < status.length(); i++) 
    {
        if (rank == 0) 
        {
            cout << "Legend" << endl;
            return 0;
        }

        char currGame = status[i];
        int starRank = rankLevel(rank);

        if (currGame == 'W') 
        {
            consecutive++;
            if (consecutive >= 3 && rank >= 6) 
            {
                stars += 2;
            } 
            else 
            {
                stars++;
            }
            if (stars > starRank) 
            {
                rank--;
                stars -= starRank;
            }
        } 
        else 
        { 
            consecutive = 0;

            if (rank == 20) 
            {
                if (stars > 0) 
                {
                    stars--;
                }
            } 
            else if (rank < 20) 
            {
                if (stars == 0) 
                {
                    rank++;
                    stars = rankLevel(rank) - 1;
                } 
                else 
                {
                    stars--;
                }
            }
        }
    }

    if (rank == 0) 
    {
        cout << "Legend" << endl;
    } 
    else 
    {
        cout << rank << endl;
    }
    return 0;
}