#include<stdio.h>
int main()
{
    int n;
    printf("enter the number");
    scanf("%d",&n);
    if(n>99 && n<1000)
    {
        printf("the number is 3 digit number");
    }
    else{
        printf("the number is not 3 dig number");
    }
    return 0;
}
