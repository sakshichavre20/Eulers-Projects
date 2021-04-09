#include<iostream>
using namespace std;
int main(){
    int sum=0,n1=0,n2=1,count=0,num;
    cout<<"enter a number : "<<endl;
    cin>>num;
    if(num <=0 ){
        cout<<"enter a positive number"<<endl;
    }
    else if( num == 1){
        cout << "Fibonacci sequence is : 1" << endl;
    }
    else{
        cout << "Fibonacci sequence is : " << endl;
        while(count<num){
            cout << n1 << endl;
            sum=n1+n2;
            n1=n2;
            n2=sum;
            count=count+1;
        }
    }
    return 0;
}