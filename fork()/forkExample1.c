#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// Driver code -> Prints Hello, World! twice
int main()
{
    // Create a child process
    fork();
    printf("Hello, World!\n");
    return 0;
}

// Output:
// Hello, World!
// Hello, World!
