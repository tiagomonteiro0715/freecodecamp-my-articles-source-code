#include<stdio.h>

int main() {

    int justin = 30;
    int *calling_justin = &justin;

    printf("%d\n", justin);
    
    printf("%d\n", *calling_justin);

    return 0;
}
