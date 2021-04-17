#include<iostream>
using namespace std;

int main(){
    int i, sq, j, sum1 = 0, sum2 = 0, sq1, result;
    for (i = 1; i < 101; i++)
    {
        sq = i * i;
        sum1 = sum1 + sq;
    }
    for (i = 1; i < 101; i++)
    {
        sum2 = sum2 + i;
    }
    sq1 = sum2 * sum2;

    result = sq1 - sum1;
    cout<<result;

    return 0;
}