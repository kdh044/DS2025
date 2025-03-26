#include <stdio.h>
#define MAX_SIZE 10

void sub(int x, int arr[])
{
    x = 10;
    arr[0] = 10;
}

void main()
{
    int var = 0, list[MAX_SIZE];
    list[0] = 0;
    sub(var , list);
    printf("var = %d\n", var);     // var 값 출력
    printf("list[0] = %d\n", list[0]);  // list[0] 값 출력
    return 0;
    //var = 0, list[0] = 10
}