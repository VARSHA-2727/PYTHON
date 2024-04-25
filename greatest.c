#include<stdio.h>
int main()
{
    int a;
    printf("enter the number");
    scanf("%d",&a);
     int b;
    printf("enter the number for b");
    scanf("%d",&b);
     int c;
    printf("enter the number for c");
    scanf("%d",&c);
    if(a>b&&a>c)
    {
        printf("A is greater");
    }
    else{
        printf("A is not greater");
    }
    if(b>a&&b>c)
    {
        printf("b is greater");
    }
    else{
        printf("b is not greater");
    }
    if(c>a&&c>b)
    {
        printf("c is greater");
    }
    else{
        printf("c is not greater");
    }
    return 0;
}
