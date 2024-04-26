#include<stdio.h>
int main()
{
    int n;
    printf("enter a positive integer");
    scanf("%d",&n);
    if(n%5==0||n%3==0)
    {
        if(n%15!=0){
        printf("the number is either divisible by 3 or 5 but not 15");
    }
    else{
        printf("the number is not divisible by 3 or 5");
    }
    }
    return 0;
}
