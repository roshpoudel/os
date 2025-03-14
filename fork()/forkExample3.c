#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    if (fork() && fork()) {
        fork();
        printf("Hello!\n");
    }
    return 0;
}