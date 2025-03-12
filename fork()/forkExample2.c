#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// Driver code -> Prints Hello, World! twice
int main()
{
    // Create 2 child processes
    fork();
    fork();
    printf("Hello, World!\n");
    return 0;
}

// Output:
// Hello, World!
// Hello, World!
// Hello, World!
// Hello, World!