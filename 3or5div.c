#include<stdio.h>
int main(){
    int i,sum=0,count=0;
    for(i=1;i<1000;i++){
        if(i%3==0 || i%5==0){
            sum=sum+i;
            count++;
        }
    }
    printf("%d \n",sum);
    printf("%d \n",count);
}