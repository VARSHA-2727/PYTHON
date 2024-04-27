#include<stdio.h>
int main()
{
    int x,y;
    printf("enter the co ordinates");
    scanf("%d %d",&x,&y);
    if(y==0 && x==0){
        printf("lies on origin");
    }
    else if(y==0){
        printf("lies on x axis");
    }
    else{
            printf("lise on y axis");
        }
    return 0;
}
