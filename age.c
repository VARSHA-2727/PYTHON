#include<stdio.h>
int main()
{
    int a;
    printf("enter the age of RAM :");
    scanf("%d",&a);
    int b;
    printf("enter the age of SHYAM :");
    scanf("%d",&b);
    int c;
    printf("enter the age of AJAY :");
    scanf("%d",&c);
    if(a<c&&a<b)
    {
        printf("%d RAM is youngest",a);
    }
    if(b<c&&b<a)
    {
       printf("%d SHYAM is youngest",b); 
    }
    if(c<a&&c<b)
    {
       printf("%d AJAY is youngest",c); 
    }
    return 0;
    
}
