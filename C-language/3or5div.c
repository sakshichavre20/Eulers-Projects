#include<stdio.h>
int main(){
    int i,sum=0,count=0;
    for(i=1;i<1000;i++){
        if(i%3==0 || i%5==0){
            sum=sum+i;
            count++;
        }
    }
    printf("%d The sum of numbers divisible by 3 or 5 upto 1000: \n",sum);
    printf("%d the count of numbers divisible by 3 or 5 upto 1000: \n",count);
}