#include<stdio.h>
#include<conio.h>
int main()
{
    int num,n1=0,n2=1,count=0,i,sum=0,evensum=0,oddsum=0;
    printf("Enter a number : \n");
    scanf("%d",&num);
    if(num<=0)
    {
        printf("Enter a positive number \n ");    
    } 
    else if (num == 1)
    {
        printf("Fibonacci Sequence = 1 \n ");
    }
    else
    {
        printf("Fibonacci Sequence =  \n");
        while(count<num)
        {
            printf("%d \n",n1);
            sum=n1+n2;
            n1=n2;
            n2=sum;
            count=count+1;
            if (n1 % 2 == 0)
            {
                evensum = evensum + n1;
            }
           
        }
        
    }
    
    printf("sum of even elements : %d \n",evensum);
   
    return 0;
}
