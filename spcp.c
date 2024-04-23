#include<stdio.h>
int main()
{
    int cp;
    printf("enter the cost price");
    scanf("%d",&cp);
    int sp;
    printf("enter the selling price");
    scanf("%d",&sp);
    if(cp<sp)
    {
        printf("profit");
    }
    else{
        printf("loss");
    }
    return 0;
}
