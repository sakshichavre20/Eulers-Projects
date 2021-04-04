#include<iostream>
using namespace std;
int main(){
int sum=0,i;
for(i=1;i<1000;i++){
    if(i%3==0 || i%5==0){
        sum=sum+i;
    }
}
cout << "The Sum of Numbers div by 3 or 5 upto 1000 :"<<sum;
return 0;
}