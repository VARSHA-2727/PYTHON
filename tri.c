#include<stdio.h>
int main()
{
    int a;
    printf("enter the 1st side");
    scanf("%d",&a);
    int b;
    printf("enter the 2nd side");
    scanf("%d",&b);
    int c;
    printf("enter the 3rd side");
    scanf("%d",&c);
    if(a+b>c&&a+c>b&&b+c>a)
    {
        printf("the given dimension is a triangle");
    }
    else{
        printf("it is not triangle");
    }
    return 0;
    
}
