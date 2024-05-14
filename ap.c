#include <stdio.h>

int main()
{
    float n;
    printf("enter the number");
    scanf("%f",&n);
    float a=100;
    for(float i=1;i<=n;i++){
           printf("%.2f\n",a);
           a=a/2;
    }
    return 0;
}
