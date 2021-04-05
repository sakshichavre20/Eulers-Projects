#include <stdio.h>

int main()
{
    int n, num1, num2, sum = 0, count = 0;
    printf("Enter 1st number : \n");
    scanf("%d", &num1);
    printf("Enter 2nd number : \n");
    scanf("%d", &num2);
    for (n = num1; n < num2; n++)
    {
        if (n % 3 == 0 || n % 5 == 0)
        {
            sum = sum + n;
            count++;
        }
    }
    printf("The sum of numbers : %d \n", sum);
    printf("The count of numbers : %d \n", count);
}