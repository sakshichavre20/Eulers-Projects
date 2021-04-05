#include<iostream>
using namespace std;
int main(){
int sum=0,n,i,j,count=0;
cout<<"Enter 1st number : "<<endl;
cin>>i;
cout<<"Enter 2nd Number : "<<endl;
cin>>j;
for(n=i;n<j;n++){
    if(n%3==0 || n%5==0){
        sum=sum+n;
        count++;
    }
}
cout << "The Sum of Numbers divisible by 3 or 5 : "<<sum<<endl;
cout << "The total Number of elements divisible by 3 or 5 : " << count;
return 0;
}