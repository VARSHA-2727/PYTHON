#include<stdio.h>
int main()
{
    int n;
    printf("enter the number");
    scanf("%d",&n);
    if(n/5&& n/3)
    {
        printf("the number is divisible by 3 and 5");
    }
    else{
        printf("the number is not divisible by 3 and 5");
    }
    return 0;
}
