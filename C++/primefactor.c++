#include<iostream>
#include<math.h>
using namespace std;

void primeFactors(int n)
{
    // Print the number of 2s that divide n
    while (n % 2 == 0)
    {
        cout<<2<<endl;
        n = n / 2;
    }

    for (int i = 3; i <= sqrt(n); i = i + 2)
    {
        // While i divides n, print i and divide n
        while (n % i == 0)
        {
            cout<<i<<endl;
            n = n / i;
        }
    }

    if (n > 2)
        cout<<n<<endl;
}
int main()
{
    int n;
    cout<<"Enter a number:"<<endl;
    cin>>n;
    primeFactors(n);
    return 0;
}