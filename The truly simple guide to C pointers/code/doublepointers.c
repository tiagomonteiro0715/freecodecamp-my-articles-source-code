#include<stdio.h>

int main() {

    int friend_adress= 67890;

    int *your_postal = &friend_adress;

    int **friend_postal = &your_postal;

    printf("Friend adress variable: %d \n\n", friend_adress);
    printf("Friend adress seen from double pointer: %d \n", **friend_postal);

    return 0;
}
