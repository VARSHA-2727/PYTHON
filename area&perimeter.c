#include<stdio.h>
int main()
{
    int l;
    printf("enter the length");
    scanf("%d",&l);
    int b;
    printf("enter the breadth");
    scanf("%d",&b);
    int a;
    a=l*b;
    int p;
    p=2*(l+b);
    if(a>p)
    {
        printf("area is greater than perimeter");}
        else{
            printf("area is not graeter than perimeter");
        }
    return 0;
}
